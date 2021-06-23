%global __brp_check_rpaths %{nil}
%global packname  GeodesiCL
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geometric Geodesy Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-leafpop 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-profvis 
BuildRequires:    R-CRAN-mapview 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rgdal 
Requires:         R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-leafpop 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-profvis 
Requires:         R-CRAN-mapview 

%description
Geometric geodesy functions applied to most common ellipsoids. This
package was created to streamline and facilitate their work for surveyors,
geographers, and everything related to geosciences.

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
