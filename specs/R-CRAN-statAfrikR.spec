%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statAfrikR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools for African National Statistics Institutes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survey >= 4.1
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.1.0
BuildRequires:    R-CRAN-haven >= 2.5.0
BuildRequires:    R-CRAN-readr >= 2.1.0
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-readxl >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-scales >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-survey >= 4.1
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tibble >= 3.1.0
Requires:         R-CRAN-haven >= 2.5.0
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-readxl >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-scales >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-forcats >= 1.0.0

%description
A comprehensive statistical toolbox for National Statistics Institutes
(INS) in Africa. Provides functions for survey data import ('KoboToolbox',
'ODK', 'CSPro', 'Excel', 'Stata', 'SPSS'), data processing and validation,
weighted statistical analysis (descriptive statistics, cross-tabulations,
regression, Human Development Index (HDI), Multidimensional Poverty Index
(MPI) following Alkire and Foster (2011) <doi:10.1093/oep/gpr051>,
inequalities), visualization (age pyramids, thematic maps, official
charts) and dissemination ('SDMX' export, 'DDI' metadata, anonymization,
Word/PDF reports). Designed to work in resource-constrained environments,
offline and in French.

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
