%global __brp_check_rpaths %{nil}
%global packname  IMD
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Index of Multiple Deprivation Data for the UK

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-readODS 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-readODS 

%description
Index of Multiple Deprivation for UK nations at various geographical
levels. In England, deprivation data is for Lower Layer Super Output
Areas, Middle Layer Super Output Areas, Wards, and Local Authorities based
on data from
<https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019>.
In Wales, deprivation data is for Lower Layer Super Output Areas, Middle
Layer Super Output Areas, Wards, and Local Authorities based on data from
<https://gov.wales/welsh-index-multiple-deprivation-full-index-update-ranks-2019>.
In Scotland, deprivation data is for Data Zones, Intermediate Zones, and
Council Areas based on data from <https://simd.scot>. In Northern Ireland,
deprivation data is for Super Output Areas and Local Government Districts
based on data from
<https://www.nisra.gov.uk/statistics/deprivation/northern-ireland-multiple-deprivation-measure-2017-nimdm2017>.
The 'IMD' package also provides the composite UK index developed by
<https://github.com/mysociety/composite_uk_imd>.

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
