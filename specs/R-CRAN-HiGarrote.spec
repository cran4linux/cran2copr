%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HiGarrote
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Nonnegative Garrote Method Incorporating Hierarchical Relationships

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-MaxPro 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-MaxPro 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 

%description
An implementation of the nonnegative garrote method that incorporates
hierarchical relationships among variables. The core function,
HiGarrote(), offers an automated approach for analyzing experiments while
respecting hierarchical structures among effects. For methodological
details, refer to Yu and Joseph (2024) <doi:10.48550/arXiv.2411.01383>.
This work is supported by U.S. National Science Foundation grant
DMS-2310637.

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
