%global __brp_check_rpaths %{nil}
%global packname  rgrassdoc
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Consult 'Grass GIS' Documentation in the RStudio Viewer or your Browser

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-cli 

%description
A tool for easy viewing of the documentation of 'GRASS GIS' (see
<https://grass.osgeo.org/>). Pages of the 'GRASS GIS' manuals found at
<https://grass.osgeo.org/grass78/manuals/full_index.html> and at
<https://grass.osgeo.org/grass78/manuals/addons/> can be viewed within the
Viewer pane of 'RStudio', or be opened in the user's default browser.

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
