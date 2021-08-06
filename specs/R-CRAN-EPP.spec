%global __brp_check_rpaths %{nil}
%global packname  EPP
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluation of Proximity Programs

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-osrm 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leaflet.extras 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-osrm 
Requires:         R-CRAN-deldir 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leaflet.extras 
Requires:         R-CRAN-sf 

%description
A toolbox for coverage evaluation of proximity programs.

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
