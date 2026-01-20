%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deepSTRAPP
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Test for Differences in Diversification Rates over Time

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildRequires:    R-CRAN-ape >= 5.8.0
BuildRequires:    R-methods >= 4.4.2
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-BAMMtools >= 2.1.12
BuildRequires:    R-CRAN-geiger >= 2.0.11
BuildRequires:    R-CRAN-phytools >= 2.0.0
BuildRequires:    R-CRAN-plyr >= 1.8.9
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-qpdf >= 1.4.1
BuildRequires:    R-CRAN-dunn.test >= 1.3.6
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-scales >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-cowplot >= 1.1.3
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.3
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.14
BuildRequires:    R-CRAN-coda >= 0.19.4.1
BuildRequires:    R-CRAN-cladoRcpp >= 0.15.1
Requires:         R-CRAN-ape >= 5.8.0
Requires:         R-methods >= 4.4.2
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-BAMMtools >= 2.1.12
Requires:         R-CRAN-geiger >= 2.0.11
Requires:         R-CRAN-phytools >= 2.0.0
Requires:         R-CRAN-plyr >= 1.8.9
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-qpdf >= 1.4.1
Requires:         R-CRAN-dunn.test >= 1.3.6
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-scales >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-cowplot >= 1.1.3
Requires:         R-CRAN-RColorBrewer >= 1.1.3
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-Rcpp >= 1.0.14
Requires:         R-CRAN-coda >= 0.19.4.1
Requires:         R-CRAN-cladoRcpp >= 0.15.1

%description
Employ time-calibrated phylogenies and trait/range data to test for
differences in diversification rates over evolutionary time.  Extend the
STRAPP test from BAMMtools::traitDependentBAMM() to any time step along
phylogenies. See inst/COPYRIGHTS for details on third-party code.

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
