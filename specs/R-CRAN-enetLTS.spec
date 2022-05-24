%global __brp_check_rpaths %{nil}
%global packname  enetLTS
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust and Sparse Methods for High Dimensional Linear and Binary and Multinomial Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-robustHD 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-grid 
Requires:         R-CRAN-reshape 
Requires:         R-parallel 
Requires:         R-CRAN-cvTools 
Requires:         R-stats 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-robustHD 

%description
Fully robust versions of the elastic net estimator are introduced for
linear and binary and multinomial regression, in particular high
dimensional data. The algorithm searches for outlier free subsets on which
the classical elastic net estimators can be applied. A reweighting step is
added to improve the statistical efficiency of the proposed estimators.
Selecting appropriate tuning parameters for elastic net penalties are done
via cross-validation.

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
