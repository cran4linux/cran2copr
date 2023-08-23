%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qfa
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Quantile-Frequency Analysis (QFA) of Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-RhpcBLASctl 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-RhpcBLASctl 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-quantreg 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-MASS 

%description
Quantile-frequency analysis (QFA) of univariate or multivariate time
series based on trigonometric quantile regression. See Li, T.-H. (2012)
"Quantile periodograms", Journal of the American Statistical Association,
107, 765–776, <doi:10.1080/01621459.2012.682815>; Li, T.-H. (2014) Time
Series with Mixed Spectra, CRC Press, <doi:10.1201/b15154>; Li, T.-H.
(2022) "Quantile Fourier transform, quantile series, and nonparametric
estimation of quantile spectra", <doi:10.48550/arXiv.2211.05844>.

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
