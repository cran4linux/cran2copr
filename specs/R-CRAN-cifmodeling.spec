%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cifmodeling
%global packver   0.9.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization and Polytomous Modeling of Survival and Competing Risks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-ggsurvfit 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-ggsurvfit 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-lifecycle 

%description
A publication-ready toolkit for modern survival and competing risks
analysis with a minimal, formula-based interface. Both nonparametric
estimation and direct polytomous regression of cumulative incidence
functions (CIFs) are supported. The main functions 'cifcurve()',
'cifplot()', and 'cifpanel()' estimate survival and CIF curves and produce
high-quality graphics with risk tables, censoring and competing-risk
marks, and multi-panel or inset layouts built on 'ggplot2' and
'ggsurvfit'. The modeling function 'polyreg()' performs direct polytomous
regression for coherent joint modeling of all cause-specific CIFs to
estimate risk ratios, odds ratios, or subdistribution hazard ratios at
user-specified time points. All core functions adopt a formula-and-data
syntax and return tidy and extensible outputs that integrate smoothly with
'modelsummary', 'broom', and the broader 'tidyverse' ecosystem. Key
numerical routines are implemented in C++ via 'Rcpp'.

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
