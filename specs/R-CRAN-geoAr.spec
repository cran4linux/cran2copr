%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geoAr
%global packver   0.0.1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Argentina's Spatial Data Toolbox

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-attempt 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-leaflet 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-attempt 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-leaflet 

%description
Collection of tools that facilitates data access and workflow for spatial
analysis of Argentina. Includes historical information from censuses,
administrative limits at different levels of aggregation, location of
human settlements, among others. Since it is expected that the majority of
users will be Spanish-speaking, the documentation of the package
prioritizes this language, although an effort is made to also offer
annotations in English.

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
