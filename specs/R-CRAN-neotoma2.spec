%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  neotoma2
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Working with the Neotoma Paleoecology Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-mapview 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-wk 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-mapview 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-wk 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-tidyr 

%description
Access and manipulation of data using the Neotoma Paleoecology Database.
<https://api.neotomadb.org/api-docs/>.

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
