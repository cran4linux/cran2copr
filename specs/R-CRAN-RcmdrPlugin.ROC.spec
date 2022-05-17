%global __brp_check_rpaths %{nil}
%global packname  RcmdrPlugin.ROC
%global packver   1.0-19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.19
Release:          1%{?dist}%{?buildtag}
Summary:          Rcmdr Receiver Operator Characteristic Plug-in Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 1.7.0
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-ResourceSelection 
Requires:         R-CRAN-Rcmdr >= 1.7.0
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-ResourceSelection 

%description
Rcmdr GUI extension plug-in for Receiver Operator Characteristic tools
from pROC package. Also it ads a Rcmdr GUI extension for Hosmer and
Lemeshow GOF test from the package ResourceSelection.

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
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
