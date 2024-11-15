%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LearnNonparam
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          'R6'-Based Flexible Framework for Permutation Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-compiler 
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-compiler 

%description
Implements non-parametric tests from Higgins (2004, ISBN:0534387756),
including tests for one sample, two samples, k samples, paired
comparisons, blocked designs, trends and association. Built with 'Rcpp'
for efficiency and 'R6' for flexible, object-oriented design, the package
provides a unified framework for performing or creating custom permutation
tests.

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
