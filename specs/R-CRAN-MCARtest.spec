%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MCARtest
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Nonparametric Testing of Missing Completely at Random

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-rcdd 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-Epi 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-highs 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcsdp 
BuildRequires:    R-CRAN-norm 
BuildRequires:    R-CRAN-missMethods 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-rcdd 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-Epi 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-highs 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcsdp 
Requires:         R-CRAN-norm 
Requires:         R-CRAN-missMethods 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-MASS 

%description
Provides functions for carrying out nonparametric hypothesis tests of the
MCAR hypothesis based on the theory of Frechet classes and compatibility.
Also gives functions for computing halfspace representations of the
marginal polytope and related geometric objects.

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
