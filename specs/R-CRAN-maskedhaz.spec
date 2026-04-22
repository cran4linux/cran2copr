%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  maskedhaz
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Masked-Cause Likelihood Models for Series Systems with Arbitrary Hazard Components

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-serieshaz 
BuildRequires:    R-CRAN-flexhaz 
BuildRequires:    R-CRAN-algebraic.dist 
BuildRequires:    R-CRAN-likelihood.model 
BuildRequires:    R-CRAN-maskedcauses 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
Requires:         R-CRAN-serieshaz 
Requires:         R-CRAN-flexhaz 
Requires:         R-CRAN-algebraic.dist 
Requires:         R-CRAN-likelihood.model 
Requires:         R-CRAN-maskedcauses 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 

%description
Likelihood-based inference for series systems with masked component cause
of failure, using arbitrary dynamic failure rate component distributions.
Computes log-likelihood, score, Hessian, and maximum likelihood estimates
for masked data satisfying conditions C1, C2, C3 under general component
hazard functions. Implements the 'series_md' protocol defined in the
'maskedcauses' package.

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
