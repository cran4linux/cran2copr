%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AgePopDenom
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Model Fine-Scale Age-Structured Population Data using Open-Source Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-base 
BuildRequires:    R-CRAN-rdhs 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-parallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-here 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-base 
Requires:         R-CRAN-rdhs 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-countrycode 
Requires:         R-parallel 

%description
Automate the modelling of age-structured population data using survey
data, grid population estimates and urban-rural extents.

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
