%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pavo
%global packver   2.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Perceptual Analysis, Visualization and Organization of Spectral Colour Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lightr >= 1.0
BuildRequires:    R-CRAN-geometry >= 0.4.0
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-farver 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-lightr >= 1.0
Requires:         R-CRAN-geometry >= 0.4.0
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-farver 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-viridisLite 

%description
A cohesive framework for the spectral and spatial analysis of colour
described in Maia, Eliason, Bitton, Doucet & Shawkey (2013)
<doi:10.1111/2041-210X.12069> and Maia, Gruson, Endler & White (2019)
<doi:10.1111/2041-210X.13174>.

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
