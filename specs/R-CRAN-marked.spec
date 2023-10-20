%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  marked
%global packver   1.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Mark-Recapture Analysis for Survival and Abundance Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-optimx >= 2013.8.6
BuildRequires:    R-CRAN-Rcpp >= 0.9.13
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R2admb 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-bookdown 
Requires:         R-CRAN-optimx >= 2013.8.6
Requires:         R-CRAN-Rcpp >= 0.9.13
Requires:         R-CRAN-lme4 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-R2admb 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-bookdown 

%description
Functions for fitting various models to capture-recapture data including
mixed-effects Cormack-Jolly-Seber(CJS) and multistate models and the
multi-variate state model structure for survival estimation and POPAN
structured Jolly-Seber models for abundance estimation. There are also
Hidden Markov model (HMM) implementations of CJS and multistate models
with and without state uncertainty and a simulation capability for HMM
models.

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
