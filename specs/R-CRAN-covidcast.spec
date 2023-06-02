%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  covidcast
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Client for Delphi's 'COVIDcast Epidata' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-MMWRweek 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-MMWRweek 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-xml2 

%description
Tools for Delphi's 'COVIDcast Epidata' API: data access, maps and time
series plotting, and basic signal processing. The API includes a
collection of numerous indicators relevant to the COVID-19 pandemic in the
United States, including official reports, de-identified aggregated
medical claims data, large-scale surveys of symptoms and public behavior,
and mobility data, typically updated daily and at the county level. All
data sources are documented at
<https://cmu-delphi.github.io/delphi-epidata/api/covidcast.html>.

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
