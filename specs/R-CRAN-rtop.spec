%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rtop
%global packver   0.6-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.6
Release:          1%{?dist}%{?buildtag}
Summary:          Interpolation of Data with Variable Spatial Support

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-gstat 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-units 
Requires:         R-CRAN-sp 

%description
Data with irregular spatial support, such as runoff related data or data
from administrative units, can with 'rtop' be interpolated to locations
without observations with the top-kriging method. A description of the
package is given by Skøien et al (2014) <doi:10.1016/j.cageo.2014.02.009>.

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
