%global __brp_check_rpaths %{nil}
%global packname  logitFD
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Principal Components Logistic Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.3
Requires:         R-core >= 3.4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-fda.usc 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-fda.usc 

%description
Functions for fitting a functional principal components logit regression
model in four different situations: ordinary and filtered functional
principal components of functional predictors, included in the model
according to their variability explanation power, and according to their
prediction ability by stepwise methods. The proposed methods were
developed in Escabias et al (2004) <doi:10.1080/10485250310001624738> and
Escabias et al (2005) <doi:10.1016/j.csda.2005.03.011>.

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
