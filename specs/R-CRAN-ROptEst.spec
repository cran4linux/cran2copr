%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ROptEst
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Optimally Robust Estimation

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-distrMod >= 2.8.1
BuildRequires:    R-CRAN-distr >= 2.8.0
BuildRequires:    R-CRAN-distrEx >= 2.8.0
BuildRequires:    R-CRAN-RandVar >= 1.2.0
BuildRequires:    R-CRAN-RobAStBase >= 1.2.0
BuildRequires:    R-CRAN-startupmsg >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-distrMod >= 2.8.1
Requires:         R-CRAN-distr >= 2.8.0
Requires:         R-CRAN-distrEx >= 2.8.0
Requires:         R-CRAN-RandVar >= 1.2.0
Requires:         R-CRAN-RobAStBase >= 1.2.0
Requires:         R-CRAN-startupmsg >= 1.0.0
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-grDevices 

%description
R infrastructure for optimally robust estimation in general smoothly
parameterized models using S4 classes and methods as described Kohl, M.,
Ruckdeschel, P., and Rieder, H. (2010), <doi:10.1007/s10260-010-0133-0>,
and in Rieder, H., Kohl, M., and Ruckdeschel, P. (2008),
<doi:10.1007/s10260-007-0047-7>.

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
