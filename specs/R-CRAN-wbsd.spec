%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wbsd
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Wild Bootstrap Size Diagnostics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 

%description
Implements the diagnostic "theta" developed in Poetscher and
Preinerstorfer (2020) "How Reliable are Bootstrap-based Heteroskedasticity
Robust Tests?" <doi:10.48550/arXiv.2005.04089>, which appeared as
<doi:10.1017/S0266466622000184> in Econometric Theory , Volume 39 , Issue
4 , August 2023 , pp. 789 - 847. The diagnostic "theta" can be used to
detect and weed out bootstrap-based procedures that provably have size
equal to one for a given testing problem. The implementation covers a
large variety of bootstrap-based procedures, cf. the above mentioned
article for details. A function for computing bootstrap p-values is
provided.

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
