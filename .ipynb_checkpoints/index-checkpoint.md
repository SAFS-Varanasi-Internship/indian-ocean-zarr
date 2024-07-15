# About our product

Our final product `INDIAN_OCEAN_025GRID_DAILY.zarr` is a blended dataset formated as a `.zarr` file, containing daily cleaned and interpolated data of ocean variables across multiple sources, mostly from processed NASA/NOAA and Copernicus collections. The data are on a standardized 0.25 degree grid. The dataset encompasses the Arabian Sea and Bay of Bengal: from -12 to 5 degree latitude and 42 to 102 longitude.

## Variables

* `adt`: sea surface height above geoid (m)
* `air_temp`: air temperature at 2 meters above the surface (K), from 1979 (ERA5)
* `mlotst`: mean ocean mixed layer thickness (m)
* `sla`: sea level anomaly (m)
* `so`: sea salinity concentration (m**-3 or PSL)
* `sst`: sea surface temperature (K), from 1979 (ERA5)
* `topo`: topography (m) (USGS)
* `u_curr`: u-component of total surface currents (m/s)
* `v_curr`: v-component of total surface currents (m/s)
* `ug_curr`: u-component of geostrophic surface currents (m/s)
* `vg_curr`: v-component of geostrophic surface currents (m/s)
* `u_wind`: u-component of surface wind (m/s), from 1979 (ERA5)
* `v_wind`: v-component of surface wind (m/s), from 1979 (ERA5)
* `curr_speed`: total current speed (m/s)
* `curr_dir`: total current direction (degrees)
* `wind_speed`: surface wind speed (m/s), computed from ERA5, from 1979
* `wind_dir`: surface wind direction (degrees), computed from ERA5, from 1979

### Chlorophyll variables

Part of the purpose of the dataset was to study ocean color gap-filling algorithms. Thus we include a variety of different comparison CHL datasets.

* `CHL_interp_my`: Gap-filled chlorophyll-a concentration (mg/m**3), from Oct 1997 (COP_CHL)
* `CHL_interp_my_uncertainty`: Chlorophyll-a concentration uncertainty (%)  (COP_CHL)
* `CHL_interp_my_flag`: 0=land, 1=observed, 2=interpolated, 3=NA (COP_CHL)
* `CHL_my`: Level 3 (means has gaps) chlorophyll-a concentration (mg/m**3). CHL_interp_my is created from this product. from Oct 1997 (COP_CHL)
* `CHL_my_uncertainty`: chlorophyll-a concentration uncertainty (%)  (COP_CHL)
* `CHL_my_flag`: 0=land, 1=observed, 2=NA  (COP_CHL)
* `CHL_cci`: multi-sensor chlorophyll-a concentration (mg/m**3), from Dec 1998 (CCI)
* `CHL_cci_uncertainty`: chlorophyll-a concentration uncertainty (rmsd)  (CCI)
* `CHL_dinoef`: Gap-free chlorophyll-a concentration (mg/m**3), from 2018 (DINOEF)
* `CHL_dinoef_uncertainty`: chlorophyll-a concentration uncertainty (rmsd)  (DINOEF)
* `CHL_dinoef_flag`: flag  (DINOEF)


All variables have been broadcasted to fit into the temporal range we have. Therefore, not all variable data are available at all times. Examine each individual variable before use.

## Notes

* ERA5: These are hourly data that have been averaged to daily data, with the addition of some additional hourly wind layers.
* USGS:
* COP_CHL: CHL from Copernicus. Gap-filled:  Level 3:
* CCI: Ocean Color CCI product that merges multiple sensors.
* DINEOF: NOAA MSL12 Ocean Color, science quality, VIIRS multi-sensor (SNPP + NOAA-20), chlorophyll DINEOF gap-filled analysis