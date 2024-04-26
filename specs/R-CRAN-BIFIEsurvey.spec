%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BIFIEsurvey
%global packver   3.6-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6.6
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Survey Statistics in Educational Assessment

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-miceadds 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-miceadds 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Contains tools for survey statistics (especially in educational
assessment) for datasets with replication designs (jackknife, bootstrap,
replicate weights; see Kolenikov, 2010; Pfefferman & Rao, 2009a, 2009b,
<doi:10.1016/S0169-7161(09)70003-3>, <doi:10.1016/S0169-7161(09)70037-9>);
Shao, 1996, <doi:10.1080/02331889708802523>). Descriptive statistics,
linear and logistic regression, path models for manifest variables with
measurement error correction and two-level hierarchical regressions for
weighted samples are included. Statistical inference can be conducted for
multiply imputed datasets and nested multiply imputed datasets and is in
particularly suited for the analysis of plausible values (for details see
George, Oberwimmer & Itzlinger-Bruneforth, 2016; Bruneforth, Oberwimmer &
Robitzsch, 2016; Robitzsch, Pham & Yanagida, 2016). The package
development was supported by BIFIE (Federal Institute for Educational
Research, Innovation and Development of the Austrian School System;
Salzburg, Austria).

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
