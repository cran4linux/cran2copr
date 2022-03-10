%global __brp_check_rpaths %{nil}
%global packname  biglasso
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extending Lasso Model Fitting to Big Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-bigmemory >= 4.5.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8.600
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-bigmemory >= 4.5.0
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ncvreg 
Requires:         R-methods 

%description
Extend lasso and elastic-net model fitting for ultrahigh-dimensional,
multi-gigabyte data sets that cannot be loaded into memory. It's much more
memory- and computation-efficient as compared to existing lasso-fitting
packages like 'glmnet' and 'ncvreg', thus allowing for very powerful big
data analysis even with an ordinary laptop.

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
