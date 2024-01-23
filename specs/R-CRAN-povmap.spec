%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  povmap
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extension to the 'emdi' Package

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-parallelMap 
BuildRequires:    R-CRAN-HLMdiag 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-readODS 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-saeRobust 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-bestNormalize 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-parallelMap 
Requires:         R-CRAN-HLMdiag 
Requires:         R-parallel 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-readODS 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-saeRobust 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-bestNormalize 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-sf 

%description
The R package 'povmap' supports small area estimation of means and poverty
headcount rates. It adds several new features to the 'emdi' package (see
"The R Package emdi for Estimating and Mapping Regionally Disaggregated
Indicators" by Kreutzmann et al. (2019) <doi:10.18637/jss.v091.i07>).
These include new options for incorporating survey weights, ex-post
benchmarking of estimates, two additional transformations, several new
convenient functions to assist with reporting results, and a wrapper
function to facilitate access from 'Stata'.

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
