%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  svytest
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Survey Weight Diagnostic Tests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-survey 

%description
Provides diagnostic tests for assessing the informativeness of survey
weights in regression models. Implements difference-in-coefficients tests
(Hausman 1978 <doi:10.2307/1913827>; Pfeffermann 1993
<doi:10.2307/1403631>), weight-association tests (DuMouchel and Duncan
1983 <doi:10.2307/2288185>; Pfeffermann and Sverchkov 1999
<https://www.jstor.org/stable/25051118>; Pfeffermann and Sverchkov 2003
<ISBN:9780470845672>; Wu and Fuller 2005
<https://www.jstor.org/stable/27590461>), estimating equations tests
(Pfeffermann and Sverchkov 2003 <ISBN:9780470845672>), and non-parametric
permutation tests. Includes simulation utilities replicating Wang et al.
(2023 <doi:10.1111/insr.12509>) and extensions.

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
