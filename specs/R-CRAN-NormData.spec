%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NormData
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Derivation of Regression-Based Normative Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-methods 
Requires:         R-CRAN-car 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-openxlsx 
Requires:         R-methods 

%description
Normative data are often used to estimate the relative position of a raw
test score in the population. This package allows for deriving
regression-based normative data. It includes functions that enable the
fitting of regression models for the mean and residual (or variance)
structures, test the model assumptions, derive the normative data in the
form of normative tables or automatic scoring sheets, and estimate
confidence intervals for the norms.

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
