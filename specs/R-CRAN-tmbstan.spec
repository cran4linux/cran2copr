%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tmbstan
%global packver   1.0.91
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.91
Release:          1%{?dist}%{?buildtag}
Summary:          MCMC Sampling from 'TMB' Model Object using 'Stan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-StanHeaders 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-rstantools

%description
Enables all 'rstan' functionality for a 'TMB' model object, in particular
MCMC sampling and chain visualization. Sampling can be performed with or
without Laplace approximation for the random effects. This is demonstrated
in Monnahan & Kristensen (2018) <DOI:10.1371/journal.pone.0197954>.

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
