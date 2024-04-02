%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geoperu
%global packver   0.0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Download Spatial Datasets of Peru

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-httr 
Requires:         R-methods 
Requires:         R-CRAN-sf 

%description
Provides convenient access to the official spatial datasets of Peru as
'sf' objects in R. This package includes a wide range of geospatial data
covering various aspects of Peruvian geography, such as: administrative
divisions (Source: INEI <https://ide.inei.gob.pe/>), protected natural
areas (Source: GEO ANP - SERNANP
<https://geo.sernanp.gob.pe/visorsernanp/>). All datasets are harmonized
in terms of attributes, projection, and topology, ensuring consistency and
ease of use for spatial analysis and visualization.

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
