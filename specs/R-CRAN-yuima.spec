%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  yuima
%global packver   1.15.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.15.18
Release:          1%{?dist}%{?buildtag}
Summary:          The YUIMA Project Package for SDEs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-boot >= 1.3.2
BuildRequires:    R-CRAN-calculus >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-stats4 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-glassoFast 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-boot >= 1.3.2
Requires:         R-CRAN-calculus >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-methods 
Requires:         R-CRAN-zoo 
Requires:         R-stats4 
Requires:         R-utils 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-glassoFast 
Requires:         R-CRAN-coda 

%description
Simulation and Inference for SDEs and Other Stochastic Processes.

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
