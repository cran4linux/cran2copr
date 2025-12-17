%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rpact
%global packver   4.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Confirmatory Adaptive Clinical Trial Design and Analysis

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-knitr >= 1.19
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-knitr >= 1.19
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-tools 
Requires:         R-CRAN-rlang 

%description
Design and analysis of confirmatory adaptive clinical trials with
continuous, binary, and survival endpoints according to the methods
described in the monograph by Wassmer and Brannath (2025)
<doi:10.1007/978-3-031-89669-9>. This includes classical group sequential
as well as multi-stage adaptive hypotheses tests that are based on the
combination testing principle.

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
