%global packname  VicmapR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Access Victorian Spatial Data Through Web File Services (WFS)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 0.7
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-sf >= 0.7
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-methods 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-rlang 

%description
Easily interfaces R to spatial datasets available through the Victorian
Government's WFS (Web Feature Service):
<https://services.land.vic.gov.au/catalogue/publicproxy/guest/dv_geoserver/wfs?request=getCapabilities>.
Which allows users to read in 'sf' data from these sources using lazy
evaluation.

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
