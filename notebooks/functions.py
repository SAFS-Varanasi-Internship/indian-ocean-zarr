def download_copernicus(dataset, date_start, date_end,  vars="", lat1=-12, lat2=32, lon1=42, lon2=102, path='/home/jovyan/shared/data/copernicus'):
    """
    dataset: dataset_id, example cmems_obs-oc_glo_bgc-plankton_my_l4-gapfree-multi-4km_P1D
    vars: copernicus variables to write, example ['CHL']
    date_start: formatted as YYYY-MM-DD or numpy.datetime64(
    date_end: formatted as YYYY-MM-DD (right-exclusive)
    """

    path_folder = f'{path}/{dataset}'
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)
    sliced_data_filename = '{year}{month}.nc'

    months = pd.date_range(date_start, date_end, freq="ME")
    for month in months:
        yr=month.year
        mon="{:02d}".format(month.month)
        start_date=f'{yr}-{mon}-01'
     
        export_file = sliced_data_filename.format(year = month.year, month = "{:02d}".format(month.month))

        filpath=copernicusmarine.subset(
           dataset_id = dataset,
           variables = vars,
           start_datetime = start_date,
           end_datetime = month,
           minimum_longitude = lon1,
           maximum_longitude = lon2, 
           minimum_latitude = lat1,
           maximum_latitude = lat2, 
           output_directory = path_folder,
           output_filename = export_file,
           force_download = True,
           overwrite_output_data = True
        )

def standardize_float64(ds):
    float64_vars = [i for i in ds.data_vars if ds[i].dtype=='float64' ] 
    # convert float64 to float32 for consistency
    for var in float64_vars:
        ds[var].values = ds[var].astype('float32')
    
    return ds

def standardize_chunk(ds, chunk_size=100):
    # set the chunk size to t 100 days
    for var in [i for i in ds.data_vars]:
        ds[var]=ds[var].chunk({"time": chunk_size})
    
    return ds
