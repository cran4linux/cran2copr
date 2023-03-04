%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  causal.decomp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Decomposition Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-CRAN-CBPS 
BuildRequires:    R-CRAN-PSweight 
BuildRequires:    R-CRAN-spelling 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-SuppDists 
Requires:         R-CRAN-CBPS 
Requires:         R-CRAN-PSweight 
Requires:         R-CRAN-spelling 
Requires:         R-utils 

%description
We implement causal decomposition analysis using the methods proposed by
Park, Lee, and Qin (2020) and Park, Kang, and Lee (2021+)
<arXiv:2109.06940>. This package allows researchers to use the
multiple-mediator-imputation, single-mediator-imputation, and
product-of-coefficients regression methods to estimate the initial
disparity, disparity reduction, and disparity remaining. It also allows to
make the inference conditional on baseline covariates. We also implement
sensitivity analysis for the causal decomposition analysis using R-squared
values as sensitivity parameters (Park, Kang, Lee, and Ma, 2023).

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
