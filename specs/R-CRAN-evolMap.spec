%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evolMap
%global packver   1.2.33
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.33
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic and Interactive Maps

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-sf 

%description
Dynamic and Interactive Maps with R, powered by 'leaflet'
<https://leafletjs.com>. 'evolMap' generates a web page with interactive
and dynamic maps to which you can add geometric entities (points, lines or
colored geographic areas), and/or markers with optional links between
them. The dynamic ability of these maps allows their components to evolve
over a continuous period of time or by periods.

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
