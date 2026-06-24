%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rasterpic
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Convert Digital Images to Spatially Referenced 'SpatRaster' Objects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.8.21
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-terra >= 1.8.21
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-png 
Requires:         R-tools 
Requires:         R-utils 

%description
Convert digital images to spatially referenced 'SpatRaster' objects, as
defined by the 'terra' package, using coordinates from supported spatial
input classes. Supported inputs include numeric coordinate vectors and
objects from the 'sf', 'terra' and 'stars' packages. The main function is
an S3 generic, allowing other packages to extend support to additional
spatial classes.

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
