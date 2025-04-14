%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multilevelTools
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multilevel and Mixed Effects Model Diagnostics and Effect Sizes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat >= 3.1.0
BuildRequires:    R-CRAN-JWileymisc >= 1.4.2
BuildRequires:    R-CRAN-data.table >= 1.14.6
BuildRequires:    R-CRAN-extraoperators >= 0.2.0
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-brms 
Requires:         R-CRAN-testthat >= 3.1.0
Requires:         R-CRAN-JWileymisc >= 1.4.2
Requires:         R-CRAN-data.table >= 1.14.6
Requires:         R-CRAN-extraoperators >= 0.2.0
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-brms 

%description
Effect sizes, diagnostics and performance metrics for multilevel and mixed
effects models. Includes marginal and conditional 'R2' estimates for
linear mixed effects models based on Johnson (2014)
<doi:10.1111/2041-210X.12225>.

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
