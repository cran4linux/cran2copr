%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RobExtremes
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Optimally Robust Estimation for Extreme Value Distributions

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-distrMod >= 2.8.0
BuildRequires:    R-CRAN-distrEx >= 2.8.0
BuildRequires:    R-CRAN-ROptEst >= 1.2.0
BuildRequires:    R-CRAN-RobAStBase >= 1.2.0
BuildRequires:    R-CRAN-startupmsg >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-RobAStRDA 
BuildRequires:    R-CRAN-distr 
BuildRequires:    R-CRAN-RandVar 
BuildRequires:    R-CRAN-actuar 
Requires:         R-CRAN-distrMod >= 2.8.0
Requires:         R-CRAN-distrEx >= 2.8.0
Requires:         R-CRAN-ROptEst >= 1.2.0
Requires:         R-CRAN-RobAStBase >= 1.2.0
Requires:         R-CRAN-startupmsg >= 1.0.0
Requires:         R-methods 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-RobAStRDA 
Requires:         R-CRAN-distr 
Requires:         R-CRAN-RandVar 
Requires:         R-CRAN-actuar 

%description
Optimally robust estimation for extreme value distributions using S4
classes and methods (based on packages 'distr', 'distrEx', 'distrMod',
'RobAStBase', and 'ROptEst'); the underlying theoretic results can be
found in Ruckdeschel and Horbenko, (2013 and 2012),
doi{10.1080/02331888.2011.628022} and doi{10.1007/s00184-011-0366-4}.

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
