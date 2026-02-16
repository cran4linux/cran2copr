%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  causalOT
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Transport Weights for Causal Inference

License:          GPL (== 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-Matrix >= 1.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-CBPS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lbfgsb3c 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-Matrix >= 1.5.0
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-CBPS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lbfgsb3c 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-osqp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-torch 
Requires:         R-utils 

%description
Uses optimal transport distances to find probabilistic matching estimators
for causal inference. These methods are described in Dunipace, Eric (2021)
<doi:10.48550/arXiv.2109.01991>. The package will build the weights,
estimate treatment effects, and calculate confidence intervals via the
methods described in the paper. The package also supports several other
methods as described in the help files.

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
