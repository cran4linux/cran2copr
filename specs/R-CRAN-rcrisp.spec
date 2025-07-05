%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcrisp
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Automate the Delineation of Urban River Spaces

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-CRAN-osmdata 
BuildRequires:    R-CRAN-rcoins 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstac 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-CRAN-sfnetworks 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-visor 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lwgeom 
Requires:         R-CRAN-osmdata 
Requires:         R-CRAN-rcoins 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstac 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sfheaders 
Requires:         R-CRAN-sfnetworks 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-units 
Requires:         R-CRAN-visor 

%description
Provides tools to automate the morphological delineation of riverside
urban areas, based on a method introduced in Forgaci (2018)
<doi:10.7480/abe.2018.31>. Delineation entails the identification of
corridor boundaries, segmentation of the corridor, and delineation of the
river space. The resulting delineation can be used to characterise spatial
phenomena that can be related to the river as a central element.

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
