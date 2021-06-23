%global __brp_check_rpaths %{nil}
%global packname  AROC
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Covariate-Adjusted Receiver Operating Characteristic Curve Inference

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat >= 2.0.0
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-nor1mix 
BuildRequires:    R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat >= 2.0.0
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-splines 
Requires:         R-CRAN-np 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-nor1mix 
Requires:         R-CRAN-spatstat.geom 

%description
Estimates the covariate-adjusted Receiver Operating Characteristic (AROC)
curve and pooled (unadjusted) ROC curve by different methods. Inacio de
Carvalho, V., and Rodriguez-Alvarez, M. X. (2018) <arXiv:1806.00473>.
NOTE: We have created a new package, ROCnReg, with more functionalities.
It also implements all the methods included in AROC. We, therefore,
recommend using ROCnReg (AROC will no longer be maintained).

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
