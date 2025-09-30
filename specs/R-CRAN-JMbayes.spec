%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  JMbayes
%global packver   0.9-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Modeling of Longitudinal and Time-to-Event Data under a Bayesian Approach

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-jagsUI 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-jagsUI 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-shiny 
Requires:         R-splines 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-rstantools

%description
Shared parameter models for the joint modeling of longitudinal and
time-to-event data using MCMC; Dimitris Rizopoulos (2016)
<doi:10.18637/jss.v072.i07>.

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
