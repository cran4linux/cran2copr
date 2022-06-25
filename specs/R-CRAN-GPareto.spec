%global __brp_check_rpaths %{nil}
%global packname  GPareto
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Processes for Pareto Front Estimation and Optimization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-emoa 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-KrigInv 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-DiceDesign 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-emoa 
Requires:         R-methods 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-KrigInv 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-DiceDesign 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-rgl 

%description
Gaussian process regression models, a.k.a. Kriging models, are applied to
global multi-objective optimization of black-box functions.
Multi-objective Expected Improvement and Step-wise Uncertainty Reduction
sequential infill criteria are available. A quantification of uncertainty
on Pareto fronts is provided using conditional simulations.

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
