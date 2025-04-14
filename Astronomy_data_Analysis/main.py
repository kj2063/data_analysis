from astropy.table import Table, vstack
import astropy.io.fits as fits
import pandas as pd
import os
import numpy as np

def stringify_multidim_columns(table):
    for col in table.colnames:
        if isinstance(table[col][0], (np.ndarray, list)):
            table[col] = [str(x) for x in table[col]]
    return table

def remove_multidim_columns(table):
    return table[[col for col in table.colnames if not isinstance(table[col][0], (np.ndarray, list))]]

# FITS 파일들이 저장된 디렉토리 경로
fits_dir = './sdss_fits_files/'  # 예: 이 폴더 안에 모든 .fits 파일이 있다고 가정

# 모든 fits 파일의 경로 가져오기
fits_files = [os.path.join(fits_dir, f) for f in os.listdir(fits_dir) if f.endswith('.fits')]

# SPALL 테이블을 저장할 리스트
spall_tables = []

for file in fits_files:
    with fits.open(file) as hdul:
        if 'SPALL' in hdul:
            spall_data = Table(hdul['SPALL'].data)
            filtered_spall_data = stringify_multidim_columns(spall_data)
            spall_tables.append(filtered_spall_data)
        else:
            print(f"'SPALL' extension not found in {file}")

# 테이블 합치기
if spall_tables:
    combined_table = vstack(spall_tables)
    
    # Pandas DataFrame으로 변환
    df = combined_table.to_pandas()

    # CSV로 저장
    # df.to_csv('combined_spall.csv', index=False)
    
    print(df.to_string())
else:
    print("SPALL 데이터를 포함한 파일이 없습니다.")