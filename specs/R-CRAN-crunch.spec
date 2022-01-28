%global __brp_check_rpaths %{nil}
%global packname  crunch
%global packver   1.29.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.29.0
Release:          1%{?dist}%{?buildtag}
Summary:          Crunch.io Data Tools

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.15
BuildRequires:    R-CRAN-httpcache >= 0.1.4
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-jsonlite >= 0.9.15
Requires:         R-CRAN-httpcache >= 0.1.4
Requires:         R-CRAN-abind 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-curl 
Requires:         R-grDevices 
Requires:         R-methods 

%description
The Crunch.io service <https://crunch.io/> provides a cloud-based data
store and analytic engine, as well as an intuitive web interface. Using
this package, analysts can interact with and manipulate Crunch datasets
from within R. Importantly, this allows technical researchers to
collaborate naturally with team members, managers, and clients who prefer
a point-and-click interface.

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
