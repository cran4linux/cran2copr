%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  polywog
%global packver   0.4-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrapped Basis Regression with Oracle Model Selection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ncvreg >= 2.4.0
BuildRequires:    R-CRAN-glmnet >= 1.9.5
BuildRequires:    R-CRAN-miscTools >= 0.6.12
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-ncvreg >= 2.4.0
Requires:         R-CRAN-glmnet >= 1.9.5
Requires:         R-CRAN-miscTools >= 0.6.12
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-stringr 

%description
Routines for flexible functional form estimation via basis regression,
with model selection via the adaptive LASSO or SCAD to prevent
overfitting.

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
