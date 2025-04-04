%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arcpullr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pull Data from an 'ArcGIS REST' API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-grDevices >= 4.3.3
BuildRequires:    R-graphics >= 4.3.3
BuildRequires:    R-CRAN-raster >= 3.6.30
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-jsonlite >= 1.8.9
BuildRequires:    R-CRAN-terra >= 1.8.15
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-sf >= 0.9.7
BuildRequires:    R-CRAN-DT >= 0.33
BuildRequires:    R-methods 
Requires:         R-grDevices >= 4.3.3
Requires:         R-graphics >= 4.3.3
Requires:         R-CRAN-raster >= 3.6.30
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-jsonlite >= 1.8.9
Requires:         R-CRAN-terra >= 1.8.15
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-sf >= 0.9.7
Requires:         R-CRAN-DT >= 0.33
Requires:         R-methods 

%description
Functions to efficiently query 'ArcGIS REST' APIs
<https://developers.arcgis.com/rest/>. Both spatial and SQL queries can be
used to retrieve data. Simple Feature (sf) objects are utilized to perform
spatial queries. This package was neither produced nor is maintained by
Esri.

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
