%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cft
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Climate Futures Toolbox

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-osmdata 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidync 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-epitools 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-pipeR 
BuildRequires:    R-CRAN-rlist 
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-osmdata 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidync 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-epitools 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-pipeR 
Requires:         R-CRAN-rlist 

%description
Developed as a collaboration between Earth lab and the North Central
Climate Adaptation Science Center to help users gain insights from
available climate data. Includes tools and instructions for downloading
climate data via a 'USGS' API and then organizing those data for
visualization and analysis that drive insight. Web interface for 'USGS'
API can be found at
<http://thredds.northwestknowledge.net:8080/thredds/reacch_climate_CMIP5_aggregated_macav2_catalog.html>.

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
