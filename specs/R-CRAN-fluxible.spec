%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fluxible
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Ecosystem Gas Fluxes Calculations for Closed Loop Chamber Setup

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-purrrlyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-purrrlyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-lifecycle 

%description
Processes the raw data from closed loop flux chamber (or tent) setups into
ecosystem gas fluxes usable for analysis. It goes from a data frame of gas
concentration over time (which can contain several measurements) and a
meta data file indicating which measurement was done when, to a data frame
of ecosystem gas fluxes including quality diagnostics. Functions provided
include different models (exponential as described in Zhao et al (2018)
<doi:10.1016/j.agrformet.2018.08.022>, quadratic and linear) to estimate
the fluxes from the raw data, quality assessment, plotting for visual
check and calculation of fluxes based on the setup specific parameters
(chamber size, plot area, ...).

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
