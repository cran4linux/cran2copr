%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  birdscanR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Migration Traffic Rate Calculation Package for 'Birdscan MR1' Radars

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-modi 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-RODBC 
BuildRequires:    R-CRAN-RPostgreSQL 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-maptools 
Requires:         R-methods 
Requires:         R-CRAN-modi 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-RODBC 
Requires:         R-CRAN-RPostgreSQL 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Extract data from 'Birdscan MR1' 'SQL' vertical-looking radar databases,
filter, and process them to Migration Traffic Rates (#objects per hour and
km) of, for example birds, and insects. Object classifications in the
'Birdscan MR1' databases are based on the dataset of Haest et al. (2021)
<doi:10.5281/zenodo.5734960>). Migration Traffic Rates can be calculated
separately for different height bins (with a height resolution of choice)
as well as over time periods of choice (e.g., 1/2 hour, 1 hour, 1 day,
day/night, the full time period of observation, and anything in between).
Two plotting functions are also included to explore the data in the 'SQL'
databases and the resulting Migration Traffic Rate results. For details on
the Migration Traffic Rate calculation procedures, see Schmid et al.
(2019) <doi:10.1111/ecog.04025>.

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
