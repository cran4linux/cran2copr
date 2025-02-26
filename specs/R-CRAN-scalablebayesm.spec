%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scalablebayesm
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Distributed Markov Chain Monte Carlo for Bayesian Inference in Marketing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-bayesm 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-parallel 
Requires:         R-CRAN-bayesm 

%description
Estimates unit-level and population-level parameters from a hierarchical
model in marketing applications. The package includes: Hierarchical Linear
Models with a mixture of normals prior and covariates, Hierarchical
Multinomial Logits with a mixture of normals prior and covariates,
Hierarchical Multinomial Logits with a Dirichlet Process prior and
covariates. For more details, see Bumbaca, F. (Rico), Misra, S., & Rossi,
P. E. (2020) <doi:10.1177/0022243720952410> "Scalable Target Marketing:
Distributed Markov Chain Monte Carlo for Bayesian Hierarchical Models".
Journal of Marketing Research, 57(6), 999-1018.

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
