%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  openair
%global packver   2.18-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.18.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for the Analysis of Air Pollution Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-dplyr >= 1.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-cluster 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-mapproj 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Tools to analyse, interpret and understand air pollution data. Data are
typically regular time series and air quality measurement, meteorological
data and dispersion model output can be analysed. The package is described
in Carslaw and Ropkins (2012, <doi:10.1016/j.envsoft.2011.09.008>) and
subsequent papers.

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
