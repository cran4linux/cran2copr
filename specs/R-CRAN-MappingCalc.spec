%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MappingCalc
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mapping Calculator for EQ-5D Utility Scores

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-tibble 

%description
Provides a 'shiny' web application to map scores from clinical instruments
(PANSS, SQLS, WHODAS 2.0, PHQ-8, EQ-5D-5L) to preference-based EQ-5D-5L
health utility values using validated regression-based and beta-mixture
mapping algorithms developed from Singapore population studies. Intended
for use in health economic evaluations and cost-utility analyses. Methods
are based on: Abdin et al. (2019) <doi:10.1007/s11136-018-2037-7>, Seow et
al. (2023) <doi:10.1080/14737167.2023.2215430>, Abdin et al. (2021)
<doi:10.1186/s12888-021-03463-0>, Abdin et al. (2024)
<doi:10.1080/14737167.2024.2376100>.

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
