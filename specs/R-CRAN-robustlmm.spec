%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robustlmm
%global packver   3.2-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Linear Mixed Effects Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix >= 1.6.2
BuildRequires:    R-CRAN-lme4 >= 1.1.9
BuildRequires:    R-CRAN-robustbase >= 0.93
BuildRequires:    R-CRAN-Rcpp >= 0.12.2
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
Requires:         R-CRAN-Matrix >= 1.6.2
Requires:         R-CRAN-lme4 >= 1.1.9
Requires:         R-CRAN-robustbase >= 0.93
Requires:         R-CRAN-Rcpp >= 0.12.2
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-nlme 
Requires:         R-methods 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-parallel 
Requires:         R-CRAN-rlang 
Requires:         R-utils 

%description
Implements the Robust Scoring Equations estimator to fit linear mixed
effects models robustly. Robustness is achieved by modification of the
scoring equations combined with the Design Adaptive Scale approach.

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
