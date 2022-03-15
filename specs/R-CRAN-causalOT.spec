%global __brp_check_rpaths %{nil}
%global packname  causalOT
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Transport Weights for Causal Inference

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-approxOT 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lbfgsb3c 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-approxOT 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-lbfgsb3c 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-osqp 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-sandwich 

%description
Uses optimal transport distances to find probabilistic matching estimators
for causal inference. These methods are described in Dunipace, Eric (2021)
<arXiv:2109.01991>. The package will build the weights, estimate treatment
effects, and calculate confidence intervals via the methods described in
the paper. The package also supports several other methods as described in
the help files.

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
