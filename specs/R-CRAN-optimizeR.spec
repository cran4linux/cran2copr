%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  optimizeR
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Unified Framework for Numerical Optimizers

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-oeli >= 0.7.2
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-lbfgsb3c 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TestFunctions 
BuildRequires:    R-CRAN-ucminf 
Requires:         R-CRAN-oeli >= 0.7.2
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-lbfgsb3c 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-R6 
Requires:         R-stats 
Requires:         R-CRAN-TestFunctions 
Requires:         R-CRAN-ucminf 

%description
Provides a unified object-oriented framework for numerical optimizers in
R. Allows for both minimization and maximization with any optimizer,
optimization over more than one function argument, measuring of
computation time, setting a time limit for long optimization tasks.

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
