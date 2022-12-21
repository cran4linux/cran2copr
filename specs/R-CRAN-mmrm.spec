%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mmrm
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed Models for Repeated Measures

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-checkmate >= 2.0
BuildRequires:    R-CRAN-TMB >= 1.9.1
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-checkmate >= 2.0
Requires:         R-CRAN-TMB >= 1.9.1
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Mixed models for repeated measures (MMRM) are a popular choice for
analyzing longitudinal continuous outcomes in randomized clinical trials
and beyond; see Cnaan, Laird and Slasor (1997)
<doi:10.1002/(SICI)1097-0258(19971030)16:20%%3C2349::AID-SIM667%%3E3.0.CO;2-E>
for a tutorial and Mallinckrodt, Lane and Schnell (2008)
<doi:10.1177/009286150804200402> for a review. This package implements
MMRM based on the marginal linear model without random effects using
Template Model Builder ('TMB') which enables fast and robust model
fitting. Users can specify a variety of covariance matrices, weight
observations, fit models with restricted or standard maximum likelihood
inference, perform hypothesis testing with Satterthwaite or Kenward-Roger
adjustment, and extract least square means estimates by using 'emmeans'.

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
