%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rsubbotools
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Estimation of Subbottin and AEP Distributions (Generalized Error Distribution)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-CRAN-Rcpp 

%description
Create densities, probabilities, random numbers, quantiles, and maximum
likelihood estimation for several distributions, mainly the symmetric and
asymmetric power exponential (AEP), a.k.a. the Subbottin family of
distributions, also known as the generalized error distribution.
Estimation is made using the design of Bottazzi (2004)
<https://ideas.repec.org/p/ssa/lemwps/2004-14.html>, where the likelihood
is maximized by several optimization procedures using the 'GNU Scientific
Library (GSL)', translated to 'C++' code, which makes it both fast and
accurate. The package also provides methods for the gamma, Laplace, and
Asymmetric Laplace distributions.

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
