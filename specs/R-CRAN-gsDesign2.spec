%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gsDesign2
%global packver   1.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Group Sequential Design with Non-Constant Effect

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-npsurvSS >= 1.1.0
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gsDesign 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-r2rtf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-npsurvSS >= 1.1.0
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gsDesign 
Requires:         R-CRAN-gt 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-r2rtf 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
The goal of 'gsDesign2' is to enable fixed or group sequential design
under non-proportional hazards. To enable highly flexible enrollment,
time-to-event and time-to-dropout assumptions, 'gsDesign2' offers
piecewise constant enrollment, failure rates, and dropout rates for a
stratified population. This package includes three methods for designs:
average hazard ratio, weighted logrank tests in Yung and Liu (2019)
<doi:10.1111/biom.13196>, and MaxCombo tests. Substantial flexibility on
top of what is in the 'gsDesign' package is intended for selecting
boundaries.

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
