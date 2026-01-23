# Data Analysis Project

데이터 분석 및 머신러닝 프로젝트 모음입니다.

## 프로젝트 구조

```
data_analysis/
├── Astronomy_data_Analysis/    # 천문학 데이터 분석 프로젝트
└── exercise1/                  # 데이터 분석 및 머신러닝 연습
```

## 📁 프로젝트 설명

### 1. Astronomy_data_Analysis (Gaia 항성 데이터 분석)

Gaia 위성 데이터를 활용한 항성 데이터 분석 프로젝트입니다.

#### 주요 내용
- **데이터**: Gaia 항성 데이터셋 (G magnitude 기준 필터링)
- **분석 내용**:
  - HR 다이어그램 생성 및 분석
  - 주계열성 파라미터 범위 계산
  - 항성 분류 (별, 퀘이사, 은하)
  - 데이터 전처리 및 시각화

#### 파일 구조
- `gaia_data_analysis_final.ipynb`: 최종 분석 노트북
- `gaia_data_analysis.ipynb`: 초기 분석 노트북
- `calculate_main_sequence_star_param_range.py`: 주계열성 파라미터 계산 스크립트
- `data/`: 분석에 사용된 데이터 파일
  - `gaia_star_below_g_mag_7.csv`
  - `gaia_galaxy_below_g_mag_17.csv`
  - `gaia_quasar_below_g_mag_17.csv`
  - `gaia_for_main_sequence_star.csv`

#### 주요 분석 결과
- HR 다이어그램 시각화
- 전처리 전후 데이터 비교
- 산점도 행렬 분석

---

### 2. exercise1 (데이터 분석 및 머신러닝 연습)

다양한 데이터 분석 및 머신러닝 기법을 연습하는 프로젝트입니다.

#### 주요 내용

##### 데이터 수집 (Data Collection)
- `00.data_collection.py`: 웹 크롤링을 통한 도서 정보 수집
- `00.data_from_open_api.py`: 공공 API를 통한 데이터 수집

##### 데이터 전처리 (Data Cleaning)
- `01.data_cleaning.py`: 데이터 정제 및 전처리

##### 머신러닝 (Machine Learning)
- `02_1.machine_learning.py`: 선형 회귀 모델
- `02_2.machine_learning_quad.py`: 2차 회귀 모델

##### 딥러닝 (Deep Learning)
- `dl_cv_exercise1.ipynb`: 컴퓨터 비전 연습 1
- `dl_cv_exercise2_1.ipynb`: 컴퓨터 비전 연습 2-1
- `dl_cv_exercise2_2.ipynb`: 컴퓨터 비전 연습 2-2
- `dl_nlp_exercise.ipynb`: 자연어 처리 연습

#### 데이터
- 도서관 장서 대출목록 데이터
- 전처리된 병합 데이터

#### 저장된 모델
- `best_cv_model.h5`: 최적 컴퓨터 비전 모델
- `best_nle_model.h5`: 최적 자연어 처리 모델

---

## 🛠️ 사용 기술

### 데이터 분석
- **pandas**: 데이터 조작 및 분석
- **numpy**: 수치 연산
- **matplotlib**: 데이터 시각화
- **seaborn**: 통계 시각화

### 머신러닝
- **scikit-learn**: 전통적인 머신러닝 알고리즘
  - Linear Regression
  - Train/Test Split
  - 평가 지표 (MAE 등)

### 딥러닝
- **TensorFlow/Keras**: 딥러닝 모델 구축
- **GPU 지원**: CUDA를 활용한 가속 학습

### 웹 스크래핑
- **requests**: HTTP 요청
- **BeautifulSoup**: HTML 파싱
- **chardet**: 인코딩 감지

---

## 📋 요구사항

### 필수 패키지
```bash
pandas
numpy
matplotlib
scikit-learn
tensorflow
requests
beautifulsoup4
chardet
seaborn
jupyter
```

### 설치 방법
```bash
pip install pandas numpy matplotlib scikit-learn tensorflow requests beautifulsoup4 chardet seaborn jupyter
```

---

## 🚀 사용 방법

### 1. 천문학 데이터 분석
```bash
cd Astronomy_data_Analysis
jupyter notebook gaia_data_analysis_final.ipynb
```

### 2. 머신러닝 연습
```bash
cd exercise1
# 데이터 수집
python 00.data_collection.py

# 데이터 전처리
python 01.data_cleaning.py

# 머신러닝 모델 학습
python 02_1.machine_learning.py
python 02_2.machine_learning_quad.py
```

### 3. 딥러닝 연습
```bash
cd exercise1
jupyter notebook dl_cv_exercise1.ipynb
jupyter notebook dl_nlp_exercise.ipynb
```

---

## 📊 주요 결과물

### 천문학 데이터 분석
- HR 다이어그램 시각화
- 주계열성 파라미터 분석
- 항성 분류 결과

### 머신러닝 연습
- 선형/2차 회귀 모델 성능 평가
- 데이터 전처리 파이프라인

### 딥러닝 연습
- 컴퓨터 비전 모델 (이미지 분류)
- 자연어 처리 모델

---

## 📝 참고 자료

- [Gaia 데이터](https://www.cosmos.esa.int/web/gaia)
- [TensorFlow 문서](https://www.tensorflow.org/)
- [scikit-learn 문서](https://scikit-learn.org/)

---

## 📄 라이선스

이 프로젝트는 개인 학습 및 연구 목적으로 작성되었습니다.

---

## 👤 작성자

데이터 분석 및 머신러닝 학습 프로젝트
