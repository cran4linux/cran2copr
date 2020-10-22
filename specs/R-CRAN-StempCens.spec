%global packname  StempCens
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Estimation and Prediction for Censored/Missing Responses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-MCMCglmm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-distances 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-MCMCglmm 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-distances 
Requires:         R-CRAN-Rdpack 

%description
It estimates the parameters of a censored or missing data in
spatio-temporal models using the SAEM algorithm (Delyon et al., 1999).
This algorithm is a stochastic approximation of the widely used EM
algorithm and an important tool for models in which the E-step does not
have an analytic form. Besides the expressions obtained to estimate the
parameters to the proposed model, we include the calculations for the
observed information matrix using the method developed by Louis (1982). To
examine the performance of the fitted model, case-deletion measure are
provided.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
