%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jollofR
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Small Area Population Estimation by Demographics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-utils 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-reshape2 
Requires:         R-utils 

%description
Automatic disaggregation of small1area population estimates by demographic
groups (e.g., age, sex, race, marital status, educational level, etc)
along with the estimates of uncertainty, using advanced Bayesian
statistical modelling approaches based on integrated nested Laplace
approximation (INLA) Rue et al. (2009)
<doi:10.1111/j.1467-9868.2008.00700.x> and stochastic partial differential
equation (SPDE) methods Lindgren et al. (2011)
<doi:10.1111/j.1467-9868.2011.00777.x>. The package implements
hierarchical Bayesian modeling frameworks for small area estimation as
described in Leasure et al. (2020) <doi:10.1073/pnas.1913050117> and
Nnanatu et al. (2025) <doi:10.1038/s41467-025-59862-4>.

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
