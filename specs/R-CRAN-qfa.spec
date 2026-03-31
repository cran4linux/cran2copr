%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qfa
%global packver   5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantile-Frequency Analysis (QFA) of Time Series and Spline Quantile Regression (SQR)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-RhpcBLASctl 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-splines 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-CRAN-piqp 
BuildRequires:    R-CRAN-boot 
Requires:         R-CRAN-RhpcBLASctl 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-SparseM 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-quantreg 
Requires:         R-splines 
Requires:         R-graphics 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-osqp 
Requires:         R-CRAN-piqp 
Requires:         R-CRAN-boot 

%description
Implementation of quantile frequency analysis (QFA) for time series based
on trigonometric quantile regression and of spline quantile regression
(SQR) for estimating the coefficients in linear quantile regression models
as smooth functions of the quantile level. References: [1] Li, T.-H.
(2012). ''Quantile periodograms,'' J. of the American Statistical
Association, 107, 765–776. <doi:10.1080/01621459.2012.682815> [2] Li,
T.-H. (2014). Time Series with Mixed Spectra, CRC Press.
<doi:10.1201/b15154> [3] Li, T.-H. (2025). ''Quantile Fourier transform,
quantile series, and nonparametric estimation of quantile spectra,''
Communications in Statistics: Simulation and Computation, 1–22.
<doi:10.1080/03610918.2025.2509820> [4] Li, T.-H. (2025).
''Quantile-crossing spectrum and spline autoregression estimation,''
Statistical Inference for Stochastic Processes, 28, 20.
<doi:10.1007/s11203-025-09336-7> [5] Li, T.-H. (2025). ''Spline
autoregression method for estimation of quantile spectrum,'' J. of
Computational and Graphical Statistics, 1-15.
<doi:10.1080/10618600.2025.2549452> [6] Li, T.-H., and Megiddo, N. (2026).
''Spline quantile regression,'' J. of Statistical Theory and Practice, 20,
30. <doi:10.1007/s42519-026-00545-8> [7] Li, T.-H. (2026). ''Spline
quantile regression with cubic and linear smoothing splines,''
<doi:10.48550/arXiv.2603.22408>.

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
