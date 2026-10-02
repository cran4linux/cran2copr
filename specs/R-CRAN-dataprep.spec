%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dataprep
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Fast, Efficient, and Versatile Data Preprocessing and Reshaping with 'C++', 'OpenMP' & 'SIMD'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-parallel 

%description
Fast, efficient, and versatile preprocessing and reshaping of tabular and
time-series data. Most heavy routines are implemented in 'C++' via 'Rcpp',
with optional 'OpenMP' parallelization and 'SIMD' acceleration ('AVX2' /
'AVX-512') on supported hardware. The 0.1.8 release rewrites the cleaning
routines in 'C++' and delivers a 1.1–1146× speedup over 0.1.5. The
'melt()' and 'dcast()' reshaping functions achieve a 0.6×–1628.9× speedup
for 'melt()' and a 1.9×–799.8× speedup for 'dcast()' relative to every one
of the seven major alternatives in the R and Python ecosystems, at every
tested scale (from 1,000 to 100,000,000 rows), and produce output
identical to 'reshape2', 'data.table', 'tidyr', 'pandas', 'polars',
'dask', and 'duckdb'. Core preprocessing steps include variable deletion
by missing fraction, observation deletion by consecutive missing runs,
point-by-point weighted outlier removal via conditional extremum,
traditional percentile-based outlier removal, and linear interpolation
within short time periods. The package also provides fast reshaping,
descriptive statistics, missing-value diagnosis, multiple imputation
strategies, winsorization, several outlier detection methods (IQR, MAD,
percentile), data transformation and standardization, categorical
encoding, duplicate removal, data validation, data quality reporting, and
stratified sampling. Feature-engineering helpers cover binning,
high-correlation and low-variance filtering, and string cleaning.
Time-series tools cover detrending, diurnal-cycle removal, rolling
statistics, lag creation, resampling, simple decomposition, day/night and
season flags, log returns, drift detection, and panel balancing.
Fit/transform-style machine-learning interfaces prevent data leakage
during preprocessing. Methods are based on, and improved from: Liang,
C.-S., Wu, H., Li, H.-Y., Zhang, Q., Li, Z. & He, K.-B. (2020)
<doi:10.1016/j.scitotenv.2020.140923>. This work was supported by the
National Natural Science Foundation of China (No. 12301674).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
