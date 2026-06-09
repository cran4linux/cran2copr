%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iDIFr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Intersectional Differential Item Functioning Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-strucchange 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-generics 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-strucchange 

%description
A toolkit for detecting Differential Item Functioning (DIF) using Logistic
Regression (LR) as described in Swaminathan and Rogers (1990)
<doi:10.1111/j.1745-3984.1990.tb00754.x>, the IRT Likelihood Ratio Test
(LRT) following Thissen, Steinberg & Wainer (1993, ISBN:0-8058-0972-4),
and model-based recursive partitioning (MOB) as implemented in
'strucchange' following Strobl, Kopf and Zeileis (2015)
<doi:10.1007/s11336-013-9388-3>. Designed for both standard two-group and
intersectional multi-group designs, 'iDIFr' prioritises effect size
reporting alongside statistical significance, clear guidance on group
construction, and interpretable output suitable for applied testing
contexts. Built-in Intersectional Contrast Analysis (ICA) classifies items
as amplified, pure-intersection, obscured, or none by comparing
single-variable and intersectional analyses.

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
