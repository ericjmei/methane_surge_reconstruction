"""Conservation and limiting cases for functions reused in comparisons."""

import numpy as np
import pytest
import xarray as xr

from src.budget import anomaly, constant_budget, decompose, oh_forcing_from_removal


def test_budget_closes_with_cross_term_other_loss_and_soil():
    data = xr.Dataset(
        {
            "mass": ("year", [5000.0, 5060.0, 5110.0]),
            "emissions": ("year", [570.0, 600.0, 592.0]),
            "k_oh": ("year", [0.09, 0.088, 0.089]),
            "k_other": ("year", [0.012, 0.013, 0.011]),
            "soil": ("year", [35.0, 34.0, 36.0]),
        },
        coords={"year": [2019, 2020, 2021]},
    )
    result = decompose(data)
    np.testing.assert_allclose(
        result.linear_growth + result.neglected, result.exact_growth, atol=1e-12
    )
    assert result.oh_forcing.sel(year=2020).item() == pytest.approx(10.0)
    assert result.burden_adjustment.sel(year=2020).item() == pytest.approx(6.12)
    xr.testing.assert_allclose(
        oh_forcing_from_removal(data.k_oh * data.mass, data.mass),
        result.oh_forcing.drop_attrs(),
    )
    assert result.relaxation_anomaly.sel(year=2019).item() == 0


def test_no_forcing_still_allows_growth_and_increased_removal():
    data = xr.Dataset(
        {
            "mass": ("year", [5000.0, 5040.0]),
            "emissions": ("year", [570.0, 570.0]),
            "k_oh": ("year", [0.09, 0.09]),
            "k_other": ("year", [0.01, 0.01]),
            "soil": ("year", [30.0, 30.0]),
        },
        coords={"year": [2019, 2020]},
    )
    result = decompose(data)
    np.testing.assert_allclose(result.relaxation, [40.0, 36.0])
    np.testing.assert_allclose(result.emission_forcing + result.oh_forcing, 0)
    np.testing.assert_allclose(result.neglected, 0)


def test_counterfactual_initial_condition_equilibrium_and_no_loss():
    t = np.array([0, 1, 10, 1000])
    assert constant_budget(t, 5000, 570, 30, 0.1)[0] == 5000
    assert constant_budget(t, 5000, 570, 30, 0.1)[-1] == pytest.approx(5400)
    np.testing.assert_allclose(constant_budget(t, 5400, 570, 30, 0.1), 5400)
    np.testing.assert_allclose(constant_budget(t, 5000, 570, 30, 0), 5000 + 540 * t)
    np.testing.assert_allclose(
        constant_budget(t, 5000, 570, 30, 1e-14), 5000 + 540 * t, rtol=1e-10
    )


def test_anomaly_uses_each_reconstruction_baseline_and_requires_it():
    values = xr.DataArray(
        [[10, 13], [100, 102]],
        dims=["reconstruction", "year"],
        coords={"year": [2019, 2020]},
    )
    np.testing.assert_allclose(anomaly(values), [[0, 3], [0, 2]])
    with pytest.raises(ValueError, match="2019"):
        anomaly(values.sel(year=[2020]))
