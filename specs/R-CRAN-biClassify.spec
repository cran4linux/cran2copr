%global packname  biClassify
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Binary Classification Using Extensions of Discriminant Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-DAAG 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-MASS 
Requires:         R-datasets 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-DAAG 

%description
Implements methods for sample size reduction within Linear and Quadratic
Discriminant Analysis in Lapanowski and Gaynanova (2020)
<arXiv:2005.03858>. Also includes methods for non-linear discriminant
analysis with simultaneous sparse feature selection in Lapanowski and
Gaynanova (2019) PMLR 89:1704-1713.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
