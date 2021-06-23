%global __brp_check_rpaths %{nil}
%global packname  strucchangeRcpp
%global packver   1.5-3-1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3.1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Testing, Monitoring, and Dating Structural Changes: C++ Version

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-sandwich 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
A fast implementation with additional experimental features for testing,
monitoring and dating structural changes in (linear) regression models.
'strucchangeRcpp' features tests/methods from the generalized fluctuation
test framework as well as from the F test (Chow test) framework. This
includes methods to fit, plot and test fluctuation processes (e.g.
cumulative/moving sum, recursive/moving estimates) and F statistics,
respectively. These methods are described in Zeileis et al. (2002)
<doi:10.18637/jss.v007.i02>. Finally, the breakpoints in regression models
with structural changes can be estimated together with confidence
intervals, and their magnitude as well as the model fit can be evaluated
using a variety of statistical measures.

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
