from astropy.io import fits

fits_file_data = fits.open('./gaia_fits_files/GaiaSource_000-000-000.fits')

print(fits_file_data.info())
