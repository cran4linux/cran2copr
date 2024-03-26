%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qtlpoly
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Random-Effect Multiple QTL Mapping in Autopolyploids

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-CRAN-gtools >= 3.9.2
BuildRequires:    R-CRAN-ggplot2 >= 3.1
BuildRequires:    R-CRAN-abind >= 1.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RLRsim 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mappoly 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-CRAN-gtools >= 3.9.2
Requires:         R-CRAN-ggplot2 >= 3.1
Requires:         R-CRAN-abind >= 1.4
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-RLRsim 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-quadprog 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-mappoly 

%description
Performs random-effect multiple interval mapping (REMIM) in full-sib
families of autopolyploid species based on restricted maximum likelihood
(REML) estimation and score statistics, as described in Pereira et al.
(2020) <doi:10.1534/genetics.120.303080>.

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
