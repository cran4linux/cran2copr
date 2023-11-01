%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cv
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Validation of Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nlme 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-car 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nlme 

%description
Cross-validation methods of regression models that exploit features of
various modeling functions to improve speed. Some of the methods
implemented in the package are novel, as described in the package
vignettes; for general introductions to cross-validation, see, for
example, Gareth James, Daniela Witten, Trevor Hastie, and Robert
Tibshirani (2021, ISBN 978-1-0716-1417-4, Secs. 5.1, 5.3), "An
Introduction to Statistical Learning with Applications in R, Second
Edition", and Trevor Hastie, Robert Tibshirani, and Jerome Friedman (2009,
ISBN 978-0-387-84857-0, Sec. 7.10), "The Elements of Statistical Learning,
Second Edition".

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
