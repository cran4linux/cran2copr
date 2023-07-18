%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eph
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Argentina's Permanent Household Survey Data and Manipulation Utilities

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-expss 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-attempt 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-expss 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-attempt 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-httr 

%description
Tools to download and manipulate the Permanent Household Survey from
Argentina (EPH is the Spanish acronym for Permanent Household Survey).
e.g: get_microdata() for downloading the datasets, get_poverty_lines() for
downloading the official poverty baskets, calculate_poverty() for the
calculation of stating if a household is in poverty or not, following the
official methodology. organize_panels() is used to concatenate
observations from different periods, and organize_labels() adds the
official labels to the data. The implemented methods are based on INDEC
(2016)
<http://www.estadistica.ec.gba.gov.ar/dpe/images/SOCIEDAD/EPH_metodologia_22_pobreza.pdf>.
As this package works with the argentinian Permanent Household Survey and
its main audience is from this country, the documentation was written in
Spanish.

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
