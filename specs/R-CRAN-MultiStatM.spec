%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiStatM
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Statistical Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-arrangements 
BuildRequires:    R-CRAN-primes 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-arrangements 
Requires:         R-CRAN-primes 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
Algorithms to build set partitions and commutator matrices and their use
in the construction of multivariate d-Hermite polynomials; estimation and
derivation of theoretical vector moments and vector cumulants of
multivariate distributions; conversion formulae for multivariate moments
and cumulants. Applications to estimation and derivation of multivariate
measures of skewness and kurtosis; estimation and derivation of asymptotic
covariances for d-variate Hermite polynomials, multivariate moments and
cumulants and measures of skewness and kurtosis. The formulae implemented
are discussed in Terdik (2021, ISBN:9783030813925), "Multivariate
Statistical Methods".

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
