%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stdReg2
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Standardization for Causal Inference

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-drgee 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-drgee 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-survival 

%description
Contains more modern tools for causal inference using regression
standardization. Four general classes of models are implemented;
generalized linear models, conditional generalized estimating equation
models, Cox proportional hazards models, and shared frailty gamma-Weibull
models. Methodological details are described in Sjölander, A. (2016)
<doi:10.1007/s10654-016-0157-3>. Also includes functionality for doubly
robust estimation for generalized linear models in some special cases, and
the ability to implement custom models.

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
