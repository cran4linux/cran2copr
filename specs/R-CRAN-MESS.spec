%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MESS
%global packver   0.5.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.12
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Esoteric Statistical Scripts

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-geeM 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggformula 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-geeM 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggformula 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-kinship2 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 

%description
A mixed collection of useful and semi-useful diverse statistical
functions, some of which may even be referenced in The R Primer book.

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
