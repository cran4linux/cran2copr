%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  frheritage
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to Get French Heritage Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-happign 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-happign 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-xml2 

%description
Get spatial vector data from the Atlas du Patrimoine
(<http://atlas.patrimoines.culture.fr/atlas/trunk/>), the official
national platform of the French Ministry of Culture, and facilitate its
use within R geospatial workflows. The package provides functions to list
available heritage datasets, query and retrieve heritage data using
spatial queries based on user-provided sf objects, perform spatial
filtering operations, and return results as sf objects suitable for
spatial analysis, mapping, and integration into heritage management and
landscape studies.

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
