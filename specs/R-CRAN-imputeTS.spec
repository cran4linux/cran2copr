%global __brp_check_rpaths %{nil}
%global packname  imputeTS
%global packver   3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Missing Value Imputation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-stinepack 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-stinepack 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp 

%description
Imputation (replacement) of missing values in univariate time series.
Offers several imputation functions and missing data plots. Available
imputation algorithms include: 'Mean', 'LOCF', 'Interpolation', 'Moving
Average', 'Seasonal Decomposition', 'Kalman Smoothing on Structural Time
Series models', 'Kalman Smoothing on ARIMA models'. Published in Moritz
and Bartz-Beielstein (2017) <doi: 10.32614/RJ-2017-009>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
