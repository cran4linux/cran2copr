%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TKApprox
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A General Framework for Bayesian Estimation Using the 'Tierney'-'Kadane' Approximation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-MASS 

%description
Provides a distribution-independent framework for Bayesian estimation of
arbitrary univariate probability models using the 'Tierney'-'Kadane'
approximation ('Tierney' & 'Kadane', 1986
<doi:10.1080/01621459.1986.10478240>). Users specify the probability
distribution, likelihood, prior distributions, and censoring mechanism,
while the package automatically constructs the posterior distribution,
computes posterior modes and Hessian matrices, approximates posterior
expectations under several Bayesian loss functions, and returns Bayesian
parameter estimates, posterior covariance matrices, credible intervals,
diagnostic plots, and model comparison statistics. Supports complete,
right-, left-, interval-, Type-I, Type-II, progressive Type-II, hybrid,
and doubly censored data ('Lawless', 2003 <ISBN:978-0-471-37215-8>;
'Meeker' & 'Escobar', 1998 <ISBN:978-0-471-14328-4>; 'Balakrishnan' &
'Aggarwala', 2000 <ISBN:978-0-8176-4129-0>; 'Kundu' & 'Pradhan', 2009
<doi:10.1198/TECH.2009.0019>), making it a flexible tool for Bayesian
reliability, survival, and lifetime data analysis.

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
