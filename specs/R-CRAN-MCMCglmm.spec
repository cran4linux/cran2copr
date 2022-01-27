%global __brp_check_rpaths %{nil}
%global packname  MCMCglmm
%global packver   2.33
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.33
Release:          1%{?dist}%{?buildtag}
Summary:          MCMC Generalised Linear Mixed Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-tensorA 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-tensorA 
Requires:         R-CRAN-cubature 
Requires:         R-methods 

%description
Fits Multivariate Generalised Linear Mixed Models (and related models)
using Markov chain Monte Carlo techniques (Hadfield 2010 J. Stat. Soft.).

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
