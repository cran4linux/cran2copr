%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lamle
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Likelihood Estimation of Latent Variable Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-methods 

%description
Approximate marginal maximum likelihood estimation of multidimensional
latent variable models via adaptive quadrature or Laplace approximations
to the integrals in the likelihood function, as presented for confirmatory
factor analysis models in Jin, S., Noh, M., and Lee, Y. (2018)
<doi:10.1080/10705511.2017.1403287>, for item response theory models in
Andersson, B., and Xin, T. (2021) <doi:10.3102/1076998620945199>, and for
generalized linear latent variable models in Andersson, B., Jin, S., and
Zhang, M. (2023) <doi:10.1016/j.csda.2023.107710>. Models implemented
include the generalized partial credit model, the graded response model,
and generalized linear latent variable models for Poisson,
negative-binomial and normal distributions. Supports a combination of
binary, ordinal, count and continuous observed variables and multiple
group models.

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
