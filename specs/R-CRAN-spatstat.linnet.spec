%global packname  spatstat.linnet
%global packver   1.65-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.65.3
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Networks Functionality of the 'spatstat' Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-spatstat.geom >= 1.65.0
BuildRequires:    R-CRAN-spatstat.core >= 1.65.0
BuildRequires:    R-CRAN-spatstat.data >= 1.4.2
BuildRequires:    R-CRAN-spatstat.utils >= 1.17.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-spatstat.geom >= 1.65.0
Requires:         R-CRAN-spatstat.core >= 1.65.0
Requires:         R-CRAN-spatstat.data >= 1.4.2
Requires:         R-CRAN-spatstat.utils >= 1.17.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 

%description
This is a subset of the 'spatstat' package, containing its functionality
for spatial data on a linear network.

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
