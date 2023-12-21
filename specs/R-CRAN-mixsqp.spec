%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mixsqp
%global packver   0.3-54
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.54
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Quadratic Programming for Fast Maximum-Likelihood Estimation of Mixture Proportions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-irlba 

%description
Provides an optimization method based on sequential quadratic programming
(SQP) for maximum likelihood estimation of the mixture proportions in a
finite mixture model where the component densities are known. The
algorithm is expected to obtain solutions that are at least as accurate as
the state-of-the-art MOSEK interior-point solver (called by function
"KWDual" in the 'REBayes' package), and they are expected to arrive at
solutions more quickly when the number of samples is large and the number
of mixture components is not too large. This implements the "mix-SQP"
algorithm, with some improvements, described in Y. Kim, P. Carbonetto, M.
Stephens & M. Anitescu (2020) <DOI:10.1080/10618600.2019.1689985>.

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
