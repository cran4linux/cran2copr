%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OptimalBinningWoE
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Binning and Weight of Evidence Framework for Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppNumerical 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dials 

%description
High-performance implementation of 36 optimal binning algorithms (16
categorical, 20 numerical) for Weight of Evidence ('WoE') transformation,
credit scoring, and risk modeling. Includes advanced methods such as Mixed
Integer Linear Programming ('MILP'), Genetic Algorithms, Simulated
Annealing, and Monotonic Regression. Features automatic method selection
based on Information Value ('IV') maximization, strict monotonicity
enforcement, and efficient handling of large datasets via 'Rcpp'. Fully
integrated with the 'tidymodels' ecosystem for building robust machine
learning pipelines. Based on methods described in Siddiqi (2006)
<doi:10.1002/9781119201731> and Navas-Palencia (2020)
<doi:10.48550/arXiv.2001.08025>.

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
