%global packname  CVEK
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Validated Kernel Ensemble

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-limSolve 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-limSolve 

%description
Implementation of Cross-Validated Kernel Ensemble (CVEK), a flexible
modeling framework for robust nonlinear regression and hypothesis testing
based on ensemble learning with kernel-ridge estimators (Jeremiah et al.
(2017) <arXiv:1710.01406> and Wenying et al. (2018) <arXiv:1811.11025>).
It allows user to conduct nonlinear regression with minimal assumption on
the function form by aggregating nonlinear models generated from a diverse
collection of kernel families. It also provides utilities to test for the
estimated nonlinear effect under this ensemble estimator, using either the
asymptotic or the bootstrap version of a generalized score test.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
