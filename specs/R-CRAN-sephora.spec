%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sephora
%global packver   0.1.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.31
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Estimation of Phenological Parameters

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.57
BuildRequires:    R-CRAN-dtwclust >= 5.5.10
BuildRequires:    R-CRAN-eBsc >= 4.15
BuildRequires:    R-parallel >= 3.6.1
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-nlme >= 3.1.157
BuildRequires:    R-CRAN-rootSolve >= 1.8.2.3
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-spiralize >= 1.0.6
BuildRequires:    R-CRAN-doParallel >= 1.0.14
BuildRequires:    R-CRAN-ggnewscale >= 0.4.7
BuildRequires:    R-CRAN-geoTS >= 0.1.7
BuildRequires:    R-methods 
Requires:         R-CRAN-MASS >= 7.3.57
Requires:         R-CRAN-dtwclust >= 5.5.10
Requires:         R-CRAN-eBsc >= 4.15
Requires:         R-parallel >= 3.6.1
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-nlme >= 3.1.157
Requires:         R-CRAN-rootSolve >= 1.8.2.3
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-spiralize >= 1.0.6
Requires:         R-CRAN-doParallel >= 1.0.14
Requires:         R-CRAN-ggnewscale >= 0.4.7
Requires:         R-CRAN-geoTS >= 0.1.7
Requires:         R-methods 

%description
Provides functions and methods for estimating phenological dates (green
up, start of a season, maturity, senescence, end of a season and dormancy)
from (nearly) periodic Earth Observation time series. These dates are
critical points of some derivatives of an idealized curve which, in turn,
is obtained through a functional principal component analysis-based
regression model. Some of the methods implemented here are based on T.
Krivobokova, P. Serra and F. Rosales (2022)
<https://www.sciencedirect.com/science/article/pii/S0167947322000998>.
Methods for handling and plotting Earth observation time series are also
provided.

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
