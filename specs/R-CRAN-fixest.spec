%global __brp_check_rpaths %{nil}
%global packname  fixest
%global packver   0.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Fixed-Effects Estimations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-dreamerr >= 1.2.3
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-dreamerr >= 1.2.3
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-Rcpp 

%description
Fast and user-friendly estimation of econometric models with multiple
fixed-effects. Includes ordinary least squares (OLS), generalized linear
models (GLM) and the negative binomial. The core of the package is based
on optimized parallel C++ code, scaling especially well for large data
sets. The method to obtain the fixed-effects coefficients is based on
Berge (2018)
<https://wwwen.uni.lu/content/download/110162/1299525/file/2018_13>.
Further provides tools to export and view the results of several
estimations with intuitive design to cluster the standard-errors.

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
