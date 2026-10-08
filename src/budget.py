"""He et al. (2026), equation (1), without fitting or running an inversion.

Derivations: docs/derivations/annual_budget.tex and counterfactual.tex.
Mass: Tg CH4; flux: Tg CH4/year; chemical loss frequency: 1/year.
Soil uptake is positive and is excluded from chemical loss frequency.
"""

import numpy as np
import xarray as xr


def anomaly(values, baseline_year=2019):
    """Subtract each reconstruction's own baseline, retaining labeled axes."""
    if "year" not in values.dims or baseline_year not in values.year:
        raise ValueError(f"A year dimension containing {baseline_year} is required")
    if len(np.unique(values.year)) != len(values.year):
        raise ValueError("Year labels must be unique")
    return values - values.sel(year=baseline_year, drop=True)


def decompose(data, baseline_year=2019):
    """Return the three published terms and exact neglected-term diagnostic.

    Required variables: emissions, mass, k_oh, k_other, soil. Each must
    include year; other dimensions (e.g. member or reconstruction) broadcast.
    Missing quantities must remain NaN, never be replaced by zero unless a
    source explicitly prescribes zero. Input units must follow this module.
    """
    names = ("emissions", "mass", "k_oh", "k_other", "soil")
    for name in names:
        if name not in data or "year" not in data[name].dims:
            raise ValueError(f"Required annual variable: {name}")
    delta = {name: anomaly(data[name], baseline_year) for name in names}
    base = data.sel(year=baseline_year, drop=True)
    k0 = base.k_oh + base.k_other
    g0 = base.emissions - k0 * base.mass - base.soil
    relaxation = g0 - k0 * delta["mass"]
    emissions = delta["emissions"]
    oh = -base.mass * delta["k_oh"]
    neglected = (
        -base.mass * delta["k_other"]
        - (delta["k_oh"] + delta["k_other"]) * delta["mass"]
        - delta["soil"]
    )
    exact = data.emissions - (data.k_oh + data.k_other) * data.mass - data.soil
    result = xr.Dataset(
        {
            "relaxation": relaxation,
            "relaxation_anomaly": -k0 * delta["mass"],
            "emission_forcing": emissions,
            "oh_forcing": oh,
            "linear_growth": relaxation + emissions + oh,
            "exact_growth": exact,
            "neglected": neglected,
            "burden_adjustment": k0 * delta["mass"],
        }
    )
    result.attrs.update(
        baseline_year=baseline_year, method="He et al. (2026), equation (1)"
    )
    for var in result.values():
        var.attrs["units"] = "Tg CH4 yr-1"
    return result


def required_forcing(growth, mass, chemical_loss_frequency, baseline_year=2019):
    """Growth anomaly plus additional removal under 2019 chemical rates."""
    return anomaly(growth, baseline_year) + chemical_loss_frequency * anomaly(
        mass, baseline_year
    )


def oh_forcing_from_removal(removal, mass, baseline_year=2019):
    """Convert positive OH removal fluxes to baseline-burden OH forcing."""
    if bool((mass <= 0).any()):
        raise ValueError("Mass must be positive")
    return -mass.sel(year=baseline_year, drop=True) * anomaly(
        removal / mass, baseline_year
    )


def constant_budget(time, initial_mass, emissions, soil, chemical_loss_frequency):
    """Analytical constant-parameter trajectory, time in years from m(0)."""
    k = float(chemical_loss_frequency)
    if not np.isfinite(k) or k < 0:
        raise ValueError("Chemical loss frequency must be finite and nonnegative")
    time = np.asarray(time, dtype=float)
    if k == 0:
        return initial_mass + (emissions - soil) * time
    return initial_mass + (emissions - soil - k * initial_mass) * (
        -np.expm1(-k * time) / k
    )
