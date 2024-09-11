%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CTRing
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Density Profiles of Wood from CT Scan Images

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xRing 
BuildRequires:    R-CRAN-functional 
BuildRequires:    R-CRAN-oro.dicom 
Requires:         R-CRAN-xRing 
Requires:         R-CRAN-functional 
Requires:         R-CRAN-oro.dicom 

%description
Computerized tomography (CT) can be used to assess certain wood properties
when wood disks or logs are scanned. Wood density profiles (i.e.
variations of wood density from pith to bark) can yield important
information used for studies in forest resource assessment, wood quality
and dendrochronology studies. The first step consists in transforming grey
values from the scan images to density values. The packages then proposes
a unique method to automatically locate the pith by combining an adapted
Hough Transform method and a one-dimensional edge detector. Tree ring
profiles (average ring density, earlywood and latewood density, ring width
and percent latewood for each ring) are then obtained.

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
