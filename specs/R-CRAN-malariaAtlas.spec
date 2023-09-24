%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  malariaAtlas
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          An R Interface to Open-Access Malaria Data, Hosted by the 'Malaria Atlas Project'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tidyterra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tidyr 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tidyterra 

%description
A suite of tools to allow you to download all publicly available parasite
rate survey points, mosquito occurrence points and raster surfaces from
the 'Malaria Atlas Project' <https://malariaatlas.org/> servers as well as
utility functions for plotting the downloaded data.

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
