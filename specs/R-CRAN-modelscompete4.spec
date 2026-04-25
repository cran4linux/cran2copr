%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modelscompete4
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Compare Nested and Non-Nested Structural Equation Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.6
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nonnest2 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-lavaan >= 0.6
Requires:         R-stats 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nonnest2 
Requires:         R-CRAN-tidyr 

%description
A comprehensive package for comparing multiple Structural Equation Models
(SEM). Supports both nested and non-nested model comparisons, chi-square
difference tests, and extraction of multiple fit indices including AIC
(Akaike Information Criterion), BIC (Bayesian Information Criterion), CFI
(Comparative Fit Index), TLI (Tucker-Lewis Index), RMSEA (Root Mean Square
Error of Approximation), and SRMR (Standardized Root Mean Square
Residual). Built on top of the 'lavaan' package for seamless SEM model
comparison workflows. The Vuong test (Vuong, 1989) for non-nested models
is used as the statistical test.

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
