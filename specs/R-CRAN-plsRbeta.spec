%global __brp_check_rpaths %{nil}
%global packname  plsRbeta
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Partial Least Squares Regression for Beta Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-plsRglm 
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-plsRglm 
Requires:         R-CRAN-betareg 
Requires:         R-methods 

%description
Provides Partial least squares Regression for (weighted) beta regression
models (Bertrand 2013, <http://journal-sfds.fr/article/view/215>) and
k-fold cross-validation of such models using various criteria. It allows
for missing data in the explanatory variables. Bootstrap confidence
intervals constructions are also available.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
