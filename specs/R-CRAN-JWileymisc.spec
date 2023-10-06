%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  JWileymisc
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Utilities and Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.3
BuildRequires:    R-CRAN-data.table >= 1.14.8
BuildRequires:    R-CRAN-VGAM >= 1.1.9
BuildRequires:    R-CRAN-lavaan >= 0.6.16
BuildRequires:    R-CRAN-extraoperators >= 0.1.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 3.4.3
Requires:         R-CRAN-data.table >= 1.14.8
Requires:         R-CRAN-VGAM >= 1.1.9
Requires:         R-CRAN-lavaan >= 0.6.16
Requires:         R-CRAN-extraoperators >= 0.1.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-emmeans 
Requires:         R-graphics 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-mice 
Requires:         R-methods 
Requires:         R-CRAN-psych 
Requires:         R-grid 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-fst 
Requires:         R-CRAN-rlang 

%description
Miscellaneous tools and functions, including: generate descriptive
statistics tables, format output, visualize relations among variables or
check distributions, and generic functions for residual and model
diagnostics.

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
