import netCDF4
import numpy as np

flux_foss_str_annuel = 0
flux_apri_bio_str_annuel = 0
flux_apri_ocean_str_annuel = 0
flux_apos_bio_str_annuel = 0
flux_apos_ocean_str_annuel = 0

flux_foss_kla_annuel = 0
flux_apri_bio_kla_annuel = 0
flux_apri_ocean_kla_annuel = 0
flux_apos_bio_kla_annuel = 0
flux_apos_ocean_kla_annuel = 0
    
for k in range(12):
    if k <9:
        l = '0'+str(k+1)
    else:
        l = str(k+1)
    
    print ("----------------------date: 2019"+l+"--------------------------------------")

    # Initialisation
    fn = './ressources/cams73_latest_co2_flux_satellite_mm_2019'+l+'.nc'
    ds = netCDF4.Dataset(fn)
    
    long = ds['longitude'][:]
    lat = ds['latitude'][:]
    area = ds['area'][:]

    print ("----------------------port strasbourg--------------------------------------")

    # port strasbourg
    # 48.5384° N, 7.7944° E

    long_str = 7.7944
    print("longitude of strasbourg port is => "+str(long_str), '\n')

    long_str_max = 11.25
    long_str_min = 7.5

    lat_str = 48.5384
    print("latitude of strasbourg port is => "+str(lat_str), '\n')

    lat_str_max = 50.21052632
    lat_str_min = 48.31578947

    max_long_str = np.where(long >= long_str)[0]
    min_long_str = np.where(long <= long_str)[0]
    long_inters_str = [min_long_str[-1], max_long_str[0]]

    max_lat_str = np.where(lat >= lat_str)[0]
    min_lat_str = np.where(lat <= lat_str)[0]
    lat_inters_str = [min_lat_str[-1], max_lat_str[0]]

    print("intersection of indexes for the longitude is: ")
    print(long_inters_str, [long[long_inters_str[0]], long[long_inters_str[1]]],  '\n')

    print("intersection of indexes for the latitude is: ")
    print(lat_inters_str, [lat[lat_inters_str[0]], lat[lat_inters_str[1]]], '\n')


    area_str = ds['area'][lat_inters_str[0]:lat_inters_str[1], long_inters_str[0]:long_inters_str[1]][0]
    print("area of strasbourg port is => ")
    print(area_str[0], ds.variables['area'].units, '\n')

    flux_foss_str = 0
    flux_apri_bio_str = 0
    flux_apri_ocean_str = 0
    flux_apos_bio_str = 0
    flux_apos_ocean_str = 0

    for i in range(2):
        for j in range(2):
            flux_foss_str = flux_foss_str + ds['flux_foss'][lat_inters_str[i], long_inters_str[j]]
            flux_apri_bio_str = flux_apri_bio_str + ds['flux_apri_bio'][lat_inters_str[i], long_inters_str[j]]
            flux_apri_ocean_str = flux_apri_ocean_str + ds['flux_apri_ocean'][lat_inters_str[i], long_inters_str[j]]
            flux_apos_bio_str = flux_apos_bio_str + ds['flux_apos_bio'][lat_inters_str[i], long_inters_str[j]]
            flux_apos_ocean_str = flux_apos_ocean_str + ds['flux_apos_ocean'][lat_inters_str[i], long_inters_str[j]]

    flux_foss_str = flux_foss_str /4
    flux_foss_str_annuel = flux_foss_str_annuel + flux_foss_str
    
    flux_apri_bio_str = flux_apri_bio_str /4    
    flux_apri_bio_str_annuel = flux_apri_bio_str_annuel + flux_apri_bio_str
    
    flux_apri_ocean_str = flux_apri_ocean_str /4    
    flux_apri_ocean_str_annuel = flux_apri_ocean_str_annuel + flux_apri_ocean_str
    
    flux_apos_bio_str = flux_apos_bio_str /4
    flux_apos_bio_str_annuel = flux_apos_bio_str_annuel + flux_apos_bio_str
    
    flux_apos_ocean_str = flux_apos_ocean_str /4
    flux_apos_ocean_str_annuel = flux_apos_ocean_str_annuel + flux_apos_ocean_str


    print("flux_foss of strasbourg port for the month of 2019-"+l+" is => ")
    print(flux_foss_str, ds.variables['flux_foss'].units, '\n')
    print("cumul flux_foss of strasbourg port up to the month of 2019-"+l+" is => ")
    print(flux_foss_str_annuel, ds.variables['flux_foss'].units, '\n')

    print("flux_apri_bio of strasbourg port for the month of 2019-"+l+" is => ")
    print(flux_apri_bio_str, ds.variables['flux_apri_bio'].units, '\n')
    print("cumul flux_apri_bio of strasbourg port up to the month of 2019-"+l+" is => ")
    print(flux_apri_bio_str_annuel, ds.variables['flux_foss'].units, '\n')

    print("flux_apri_ocean of strasbourg port for the month of 2019-"+l+" is => ")
    print(flux_apri_ocean_str, ds.variables['flux_apri_ocean'].units, '\n')
    print("cumul flux_apri_ocean of strasbourg port up to the month of 2019-"+l+" is => ")
    print(flux_apri_ocean_str_annuel, ds.variables['flux_foss'].units, '\n')
    
    print("flux_apos_bio of strasbourg port for the month of 2019-"+l+" is => ")
    print(flux_apos_bio_str, ds.variables['flux_apos_bio'].units, '\n')
    print("cumul flux_apos_bio of strasbourg port up to the month of 2019-"+l+" is => ")
    print(flux_apos_bio_str_annuel, ds.variables['flux_foss'].units, '\n')
    
    print("flux_apos_ocean of strasbourg port for the month of 2019-"+l+" is => ")
    print(flux_apos_ocean_str, ds.variables['flux_apos_ocean'].units, '\n')
    print("cumul flux_apos_ocean of strasbourg port up to the month of 2019-"+l+" is => ")
    print(flux_apos_ocean_str_annuel, ds.variables['flux_foss'].units, '\n')

    print ("---------------------end strasbourg--------------------------------------")

    
    print ("----------------------port klaipeda--------------------------------------")

    #port klaipeda
    # 55.7063° N, 21.1251° E
    long_kla = 21.1251
    print("longitude of klaipeda port is => "+str(long_kla), '\n')


    long_kla_max = 22.5
    long_kla_min = 18.75

    lat_kla = 55.7063
    print("latitude of klaipeda port is => "+str(lat_str), '\n')

    lat_kla_max = 55.89473684
    lat_kla_min = 54.

    max_long_kla = np.where(long >= long_kla)[0]
    min_long_kla = np.where(long <= long_kla)[0]
    long_inters_kla = [min_long_kla[-1], max_long_kla[0]]

    max_lat_kla = np.where(lat >= lat_kla)[0]
    min_lat_kla = np.where(lat <= lat_kla)[0]
    lat_inters_kla = [min_lat_kla[-1], max_lat_kla[0]]

    print("intersection of indexes for the longitude is: ")
    print(long_inters_kla, [long[long_inters_kla[0]], long[long_inters_kla[1]]],  '\n')

    print("intersection of indexes for the latitude is: ")
    print(lat_inters_kla, [lat[lat_inters_kla[0]], lat[lat_inters_kla[1]]], '\n')


    area_kla = ds['area'][lat_inters_kla[0]:lat_inters_kla[1], long_inters_kla[0]:long_inters_kla[1]][0]
    print("area of klaipeda port is => ")
    print(area_kla[0], ds.variables['area'].units, '\n')

    flux_foss_kla = 0
    flux_apri_bio_kla = 0
    flux_apri_ocean_kla = 0
    flux_apos_bio_kla = 0
    flux_apos_ocean_kla = 0

    for i in range(2):
        for j in range(2):
            flux_foss_kla = flux_foss_kla + ds['flux_foss'][lat_inters_kla[i], long_inters_kla[j]]
            flux_apri_bio_kla = flux_apri_bio_kla + ds['flux_apri_bio'][lat_inters_kla[i], long_inters_kla[j]]
            flux_apri_ocean_kla = flux_apri_ocean_kla + ds['flux_apri_ocean'][lat_inters_kla[i], long_inters_kla[j]]
            flux_apos_bio_kla = flux_apos_bio_kla + ds['flux_apos_bio'][lat_inters_kla[i], long_inters_kla[j]]
            flux_apos_ocean_kla = flux_apos_ocean_kla + ds['flux_apos_ocean'][lat_inters_kla[i], long_inters_kla[j]]

    flux_foss_kla = flux_foss_kla /4
    flux_foss_kla_annuel = flux_foss_kla_annuel + flux_foss_kla
    
    flux_apri_bio_kla = flux_apri_bio_kla /4    
    flux_apri_bio_kla_annuel = flux_apri_bio_kla_annuel + flux_apri_bio_kla
    
    flux_apri_ocean_kla = flux_apri_ocean_kla /4    
    flux_apri_ocean_kla_annuel = flux_apri_ocean_kla_annuel + flux_apri_ocean_kla
    
    flux_apos_bio_kla = flux_apos_bio_kla /4
    flux_apos_bio_kla_annuel = flux_apos_bio_kla_annuel + flux_apos_bio_kla
    
    flux_apos_ocean_kla = flux_apos_ocean_kla /4
    flux_apos_ocean_kla_annuel = flux_apos_ocean_kla_annuel + flux_apos_ocean_kla


    print("flux_foss of klaipeda port for the month of 2019-"+l+" is => ")
    print(flux_foss_kla, ds.variables['flux_foss'].units, '\n')
    print("cumul flux_foss of klaipeda port up to the month of 2019-"+l+" is => ")
    print(flux_foss_kla_annuel, ds.variables['flux_foss'].units, '\n')

    print("flux_apri_bio of klaipeda port for the month of 2019-"+l+" is => ")
    print(flux_apri_bio_kla, ds.variables['flux_apri_bio'].units, '\n')
    print("cumul flux_apri_bio of klaipeda port up to the month of 2019-"+l+" is => ")
    print(flux_apri_bio_kla_annuel, ds.variables['flux_foss'].units, '\n')

    print("flux_apri_ocean of klaipeda port for the month of 2019-"+l+" is => ")
    print(flux_apri_ocean_kla, ds.variables['flux_apri_ocean'].units, '\n')
    print("cumul flux_apri_ocean of klaipeda port up to the month of 2019-"+l+" is => ")
    print(flux_apri_ocean_kla_annuel, ds.variables['flux_foss'].units, '\n')
    
    print("flux_apos_bio of klaipeda port for the month of 2019-"+l+" is => ")
    print(flux_apos_bio_kla, ds.variables['flux_apos_bio'].units, '\n')
    print("cumul flux_apos_bio of klaipeda port up to the month of 2019-"+l+" is => ")
    print(flux_apos_bio_kla_annuel, ds.variables['flux_foss'].units, '\n')
    
    print("flux_apos_ocean of klaipeda port for the month of 2019-"+l+" is => ")
    print(flux_apos_ocean_kla, ds.variables['flux_apos_ocean'].units, '\n')
    print("cumul flux_apos_ocean of klaipeda port up to the month of 2019-"+l+" is => ")
    print(flux_apos_ocean_kla_annuel, ds.variables['flux_foss'].units, '\n')


    print ("---------------------end klaipeda--------------------------------------")

