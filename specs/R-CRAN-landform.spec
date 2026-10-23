%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  landform
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Topographic Position Index-Based Landform Classification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.7.3
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-terra >= 1.7.3
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Classifies a landscape into slope-position and landform classes on the
basis of the Topographic Position Index (TPI) and slope, following Weiss
(2001) and Jenness (2006). Two classifications are offered: a six-class
Slope Position Classification, based on one TPI scale, and a ten-class
Landform Classification, based on a small and a large TPI scale. The TPI
can be computed over square, circular or annular neighbourhoods, sized in
cells or in map units, and standardised either over the whole grid (as in
the original method) or locally. Results are returned as an object holding
the classified raster, the TPI and slope surfaces, and per-class
descriptive statistics, with methods for printing, summarising and
plotting.

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
