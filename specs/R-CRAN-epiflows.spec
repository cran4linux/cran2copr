%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epiflows
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Predicting Disease Spread from Flow Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-epicontacts 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-epicontacts 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-visNetwork 

%description
Provides functions and classes designed to handle and visualise
epidemiological flows between locations. Also contains a statistical
method for predicting disease spread from flow data initially described in
Dorigatti et al. (2017) <doi:10.2807/1560-7917.ES.2017.22.28.30572>. This
package is part of the RECON (<https://www.repidemicsconsortium.org/>)
toolkit for outbreak analysis.

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
