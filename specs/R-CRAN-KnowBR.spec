%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KnowBR
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Discriminating Well Surveyed Spatial Units from Exhaustive Biodiversity Databases

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fossil 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-fossil 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-vegan 

%description
It uses species accumulation curves and diverse estimators to assess, at
the same time, the levels of survey coverage in multiple geographic cells
of a size defined by the user or polygons. It also enables the
geographical depiction of observed species richness, survey effort and
completeness values including a background with administrative areas.

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
