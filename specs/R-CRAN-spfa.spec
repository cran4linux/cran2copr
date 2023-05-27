%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spfa
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Parametric Factor Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 

%description
Estimation, scoring, and plotting functions for the semi-parametric factor
model proposed by Liu & Wang (2022) <doi:10.1007/s11336-021-09832-8> and
Liu & Wang (2023) <arXiv:2303.10079>. Both the conditional densities of
observed responses given the latent factors and the joint density of
latent factors are estimated non-parametrically. Functional parameters are
approximated by smoothing splines, whose coefficients are estimated by
penalized maximum likelihood using an expectation-maximization (EM)
algorithm. E- and M-steps can be parallelized on multi-thread computing
platforms that support 'OpenMP'. Both continuous and unordered categorical
response variables are supported.

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
