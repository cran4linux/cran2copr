%global __brp_check_rpaths %{nil}
%global packname  stacomiR
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fish Migration Monitoring

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.1.1
BuildRequires:    R-CRAN-stacomirtools >= 0.6.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-intervals 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-pool 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-Hmisc >= 4.1.1
Requires:         R-CRAN-stacomirtools >= 0.6.0
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-intervals 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RPostgres 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-lattice 
Requires:         R-grDevices 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-pool 
Requires:         R-CRAN-withr 

%description
Graphical outputs and treatment for a database of fish pass monitoring. It
is a part of the 'STACOMI' open source project developed in France by the
French Office for Biodiversity institute to centralize data obtained by
fish pass monitoring. This version is available in French and English. See
<http://stacomir.r-forge.r-project.org/> for more information on
'STACOMI'.

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
