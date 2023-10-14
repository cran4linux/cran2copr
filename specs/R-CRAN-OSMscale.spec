%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OSMscale
%global packver   0.5.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.20
Release:          1%{?dist}%{?buildtag}
Summary:          Add a Scale Bar to 'OpenStreetMap' Plots

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-berryFunctions >= 1.15.0
BuildRequires:    R-CRAN-OpenStreetMap 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-berryFunctions >= 1.15.0
Requires:         R-CRAN-OpenStreetMap 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-pbapply 

%description
Functionality to handle and project lat-long coordinates, easily download
background maps and add a correct scale bar to 'OpenStreetMap' plots in
any map projection.

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
