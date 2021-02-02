%global packname  spatstat.core
%global packver   1.65-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.65.5
Release:          1%{?dist}%{?buildtag}
Summary:          Core Functionality of the 'spatstat' Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-spatstat.data >= 1.6.1
BuildRequires:    R-CRAN-goftest >= 1.2.2
BuildRequires:    R-CRAN-spatstat.utils >= 1.18.0
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-spatstat.sparse 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-tensor 
Requires:         R-CRAN-spatstat.data >= 1.6.1
Requires:         R-CRAN-goftest >= 1.2.2
Requires:         R-CRAN-spatstat.utils >= 1.18.0
Requires:         R-CRAN-spatstat.geom 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-spatstat.sparse 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-tensor 

%description
This is a subset of the original 'spatstat' package, containing all of the
user-level code from 'spatstat', except for the code for linear networks.

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
