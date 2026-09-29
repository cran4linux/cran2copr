%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wowi
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Detect Spatial Clusters of High Rates of Acute Malnutrition

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.2.8.1
BuildRequires:    R-CRAN-tibble >= 3.3.0
BuildRequires:    R-CRAN-withr >= 3.0.2
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-shiny >= 1.11.1
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-shinycssloaders >= 1.1.0
BuildRequires:    R-CRAN-rsatscan >= 1.0.9
BuildRequires:    R-CRAN-bslib >= 0.9.0
BuildRequires:    R-CRAN-htmltools >= 0.5.8.1
BuildRequires:    R-CRAN-DT >= 0.34.0
BuildRequires:    R-CRAN-mwana >= 0.2.5
Requires:         R-CRAN-openxlsx >= 4.2.8.1
Requires:         R-CRAN-tibble >= 3.3.0
Requires:         R-CRAN-withr >= 3.0.2
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-shiny >= 1.11.1
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-shinycssloaders >= 1.1.0
Requires:         R-CRAN-rsatscan >= 1.0.9
Requires:         R-CRAN-bslib >= 0.9.0
Requires:         R-CRAN-htmltools >= 0.5.8.1
Requires:         R-CRAN-DT >= 0.34.0
Requires:         R-CRAN-mwana >= 0.2.5

%description
Utilities for detecting statistically significant spatial clusters of high
acute malnutrition rates using a Bernoulli spatial scan statistic,
implemented via the 'SaTScan' software <https://www.satscan.org/>.

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
