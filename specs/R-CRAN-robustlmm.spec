%global __brp_check_rpaths %{nil}
%global packname  robustlmm
%global packver   2.5-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Linear Mixed Effects Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-lme4 >= 1.1.9
BuildRequires:    R-CRAN-Matrix >= 1.0.13
BuildRequires:    R-CRAN-robustbase >= 0.93
BuildRequires:    R-CRAN-Rcpp >= 0.12.2
BuildRequires:    R-CRAN-cubature > 1.3.8
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-lme4 >= 1.1.9
Requires:         R-CRAN-Matrix >= 1.0.13
Requires:         R-CRAN-robustbase >= 0.93
Requires:         R-CRAN-Rcpp >= 0.12.2
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-nlme 
Requires:         R-methods 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-fastGHQuad 

%description
A method to fit linear mixed effects models robustly. Robustness is
achieved by modification of the scoring equations combined with the Design
Adaptive Scale approach.

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
