%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ToxicR
%global packver   22.8.1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          22.8.1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Toxicology Dose-Response Data

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cmake
BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-doBy >= 4.6.11
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-multcomp >= 1.4
BuildRequires:    R-CRAN-tidyverse >= 1.3.0
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-ggridges >= 0.5.3
BuildRequires:    R-CRAN-coda >= 0.19.4
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-CRAN-doBy >= 4.6.11
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-multcomp >= 1.4
Requires:         R-CRAN-tidyverse >= 1.3.0
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-ggridges >= 0.5.3
Requires:         R-CRAN-coda >= 0.19.4
Requires:         R-CRAN-forcats 

%description
Toxicology routines for analyzing dose-response data include dose-response
analysis and trend tests. Dose-Response methods are based upon the US
EPA's benchmark dose software 3.  Methods have been extended to include
additional functionality based on World Health Organization guidelines.
It further supports the European Food Safety Authority's draft guidance on
model averaging. The dose-response methods and datasets used in this
package are described in Wheeler et al. (2019) <doi:10.1111/risa.13218>,
Wheeler et al. (2020) <doi:10.1111/risa.13537>, and Wheeler et al. (2022)
<doi:10.1002/env.2728>.  NTP routines are described in Bailer and Portier
(1988) <doi:10.2307/2531856>, Bieler and Williams (1993)
<doi:10.2307/2532200>, Williams (1971) <doi:10.2307/2528930>, and Shirley
(1977) <doi:10.2307/2529789>.

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
