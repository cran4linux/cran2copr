%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nomisdata
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Access 'Nomis' UK Labour Market Data and Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-methods 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-utils 
Requires:         R-CRAN-digest 
Requires:         R-methods 

%description
Interface to the 'Nomis' database (<https://www.nomisweb.co.uk>), a
comprehensive resource of United Kingdom labour market statistics provided
by the Office for National Statistics (ONS). Facilitates programmatic
access to census data, labour force surveys, benefit statistics, and
socioeconomic indicators through a modern HTTP client with intelligent
caching, automatic query pagination, and tidy data principles. Includes
spatial data integration, interactive helpers, and visualization
utilities. Independent implementation unaffiliated with ONS or Durham
University.

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
