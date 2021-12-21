%global __brp_check_rpaths %{nil}
%global packname  aurin
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Access Datasets from the 'AURIN' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-cli >= 2.1.0
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-glue >= 1.4.0
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-sf >= 0.9.0
BuildRequires:    R-CRAN-ows4R >= 0.1
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-cli >= 2.1.0
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-glue >= 1.4.0
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-sf >= 0.9.0
Requires:         R-CRAN-ows4R >= 0.1
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 

%description
'AURIN' <https://aurin.org.au/resources/aurin-apis/> is "Australia's
single largest resource for accessing clean, integrated, spatially enabled
and research-ready data on issues surrounding health and wellbeing,
socio-economic metrics, transportation, and land-use.". This package
provides functions to download and search datasets from the AURIN API
(it's free to use!).

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
