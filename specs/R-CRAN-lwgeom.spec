%global packname  lwgeom
%global packver   0.2-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Bindings to Selected 'liblwgeom' Functions for Simple Features

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    geos-devel >= 3.3.0
BuildRequires:    proj-devel >= 4.8.0
BuildRequires:    sqlite-devel
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-sf >= 0.9.3
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-sf >= 0.9.3
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-units 

%description
Access to selected functions found in 'liblwgeom'
<https://github.com/postgis/postgis/tree/master/liblwgeom>, the
light-weight geometry library used by 'PostGIS' <http://postgis.net/>.

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
