%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesGP
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Implementation of Gaussian Process in Bayesian Hierarchical Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-TMB >= 1.9.7
BuildRequires:    R-CRAN-Matrix >= 1.6.3
BuildRequires:    R-CRAN-aghq >= 0.4.1
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-tmbstan 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-TMB >= 1.9.7
Requires:         R-CRAN-Matrix >= 1.6.3
Requires:         R-CRAN-aghq >= 0.4.1
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-tmbstan 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-methods 
Requires:         R-CRAN-rstantools

%description
Implements Bayesian hierarchical models with flexible Gaussian process
priors, focusing on Extended Latent Gaussian Models and incorporating
various Gaussian process priors for Bayesian smoothing. Computations
leverage finite element approximations and adaptive quadrature for
efficient inference. Methods are detailed in Zhang, Stringer, Brown, and
Stafford (2023) <doi:10.1177/09622802221134172>; Zhang, Stringer, Brown,
and Stafford (2024) <doi:10.1080/10618600.2023.2289532>; Zhang, Brown, and
Stafford (2023) <doi:10.48550/arXiv.2305.09914>; and Stringer, Brown, and
Stafford (2021) <doi:10.1111/biom.13329>.

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
