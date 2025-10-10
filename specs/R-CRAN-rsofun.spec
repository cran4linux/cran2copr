%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rsofun
%global packver   5.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The P-Model and BiomeE Modelling Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-BayesianTools 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-multidplyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-BayesianTools 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-multidplyr 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements the Simulating Optimal FUNctioning framework for site-scale
simulations of ecosystem processes, including model calibration. It
contains 'Fortran 90' modules for the P-model (Stocker et al. (2020)
<doi:10.5194/gmd-13-1545-2020>), SPLASH (Davis et al. (2017)
<doi:10.5194/gmd-10-689-2017>) and BiomeE (Weng et al. (2015)
<doi:10.5194/bg-12-2655-2015>).

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
