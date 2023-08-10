%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RCTrep
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Validation of Estimates of Treatment Effects in Observational Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-PSweight 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geex 
BuildRequires:    R-CRAN-BART 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-caret 
Requires:         R-base 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-PSweight 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geex 
Requires:         R-CRAN-BART 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-glue 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-caret 

%description
Validates estimates of (conditional) average treatment effects obtained
using observational data by a) making it easy to obtain and visualize
estimates derived using a large variety of methods (G-computation, inverse
propensity score weighting, etc.), and b) ensuring that estimates are
easily compared to a gold standard (i.e., estimates derived from
randomized controlled trials). 'RCTrep' offers a generic protocol for
treatment effect validation based on four simple steps, namely,
set-selection, estimation, diagnosis, and validation. 'RCTrep' provides a
simple dashboard to review the obtained results. The validation approach
is introduced by Shen, L., Geleijnse, G. and Kaptein, M. (2023)
<doi:10.21203/rs.3.rs-2559287/v1>.

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
