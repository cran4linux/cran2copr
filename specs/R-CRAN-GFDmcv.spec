%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GFDmcv
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          General Hypothesis Testing Problems for Multivariate Coefficients of Variation

License:          LGPL-2 | LGPL-3 | GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-HSAUR 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-HSAUR 

%description
Performs test procedures for general hypothesis testing problems for four
multivariate coefficients of variation (Ditzhaus and Smaga, 2023
<arXiv:2301.12009>). We can verify the global hypothesis about equality as
well as the particular hypotheses defined by contrasts, e.g., we can
conduct post hoc tests. We also provide the simultaneous confidence
intervals for contrasts.

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
