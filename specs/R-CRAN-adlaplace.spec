%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adlaplace
%global packver   0.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5
Release:          1%{?dist}%{?buildtag}
Summary:          Laplace Approximations Using Automatic Differentiation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RCppAD >= 1.20260000.0.2
BuildRequires:    R-CRAN-Matrix >= 1.2.18
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-trustOptim 
Requires:         R-CRAN-RCppAD >= 1.20260000.0.2
Requires:         R-CRAN-Matrix >= 1.2.18
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 

%description
Computes Laplace-approximate maximum likelihood for hierarchical and
latent Gaussian models. A formula interface specifies observation
densities (e.g. Gaussian, negative Binomial), fixed effects, and random
terms (independent effects, smoothing terms). Customized response
distributions and models for random effects can be specified through a
low-level interface or by writing interoperable packages. Derivatives are
computed using automatic differentiation with 'CppAD', and used in trust
region optimization to find modes of random effects. Derivatives of the
Laplace approximation of the log-likelihood are computed using third order
contractions and is compatible with custom atomics. The approach follows
Kristensen, Nielsen, Berg, Skaug, and Bell (2016)
<doi:10.18637/jss.v070.i05>.

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
