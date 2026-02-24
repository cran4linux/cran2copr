%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epiR
%global packver   2.0.91
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.91
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for the Analysis of Epidemiological Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-BiasedUrn 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-officer 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-BiasedUrn 
Requires:         R-CRAN-pander 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-flextable 
Requires:         R-stats 
Requires:         R-CRAN-officer 

%description
Tools for the analysis of epidemiological and surveillance data. Contains
functions for directly and indirectly adjusting measures of disease
frequency, quantifying measures of association on the basis of single or
multiple strata of count data presented in a contingency table,
computation of confidence intervals around incidence risk and incidence
rate estimates and sample size calculations for cross-sectional,
case-control and cohort studies. Surveillance tools include functions to
calculate an appropriate sample size for 1- and 2-stage representative
freedom surveys, functions to estimate surveillance system sensitivity and
functions to support scenario tree modelling analyses.

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
