%global packname  intamapInteractive
%global packver   1.1-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Add-on Functionality for 'intamap'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-intamap 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-intamap 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-automap 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-rgdal 
Requires:         R-methods 
Requires:         R-CRAN-sp 

%description
Includes additional functionality for spatial interpolation in the intamap
package, such as bias correction and network optimization.

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
