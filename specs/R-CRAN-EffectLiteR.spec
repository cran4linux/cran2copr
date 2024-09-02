%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EffectLiteR
%global packver   0.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Average and Conditional Effects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-lavaan >= 0.6.8
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-restriktor 
BuildRequires:    R-CRAN-ic.infer 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-lavaan >= 0.6.8
Requires:         R-methods 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-car 
Requires:         R-CRAN-restriktor 
Requires:         R-CRAN-ic.infer 
Requires:         R-CRAN-numDeriv 

%description
Use structural equation modeling to estimate average and conditional
effects of a treatment variable on an outcome variable, taking into
account multiple continuous and categorical covariates.

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
