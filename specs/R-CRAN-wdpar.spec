%global __brp_check_rpaths %{nil}
%global packname  wdpar
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the World Database on Protected Areas

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 3.2
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-RSelenium >= 1.7.4
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-progress >= 1.2.0
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-countrycode >= 1.1.0
BuildRequires:    R-CRAN-sf >= 1.0.2
BuildRequires:    R-CRAN-cli >= 1.0.1
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
BuildRequires:    R-CRAN-wdman >= 0.2.4
BuildRequires:    R-CRAN-lwgeom >= 0.2.1
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-curl >= 3.2
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-RSelenium >= 1.7.4
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-progress >= 1.2.0
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-countrycode >= 1.1.0
Requires:         R-CRAN-sf >= 1.0.2
Requires:         R-CRAN-cli >= 1.0.1
Requires:         R-CRAN-rappdirs >= 0.3.1
Requires:         R-CRAN-wdman >= 0.2.4
Requires:         R-CRAN-lwgeom >= 0.2.1
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-utils 
Requires:         R-CRAN-sp 

%description
Fetch and clean data from the World Database on Protected Areas (WDPA) and
the World Database on Other Effective Area-Based Conservation Measures
(WDOECM). Data is obtained from Protected Planet
<https://www.protectedplanet.net/en>. To augment data cleaning procedures,
users can install the 'prepr' R package (available at
<https://github.com/dickoa/prepr>).

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
