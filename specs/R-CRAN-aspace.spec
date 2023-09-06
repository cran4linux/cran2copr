%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aspace
%global packver   4.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Estimating Centrographic Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.3.0
Requires:         R-core >= 2.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-Hmisc 

%description
A collection of functions for computing centrographic statistics (e.g.,
standard distance, standard deviation ellipse, standard deviation box) for
observations taken at point locations. Separate plotting functions have
been developed for each measure. Users interested in writing results to
ESRI shapefiles can do so by using results from 'aspace' functions as
inputs to the convert.to.shapefile() and write.shapefile() functions in
the 'shapefiles' library. We intend to provide 'terra' integration for
geographic data in a future release. The 'aspace' package was originally
conceived to aid in the analysis of spatial patterns of travel behaviour
(see Buliung and Remmel 2008 <doi:10.1007/s10109-008-0063-7>).

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
