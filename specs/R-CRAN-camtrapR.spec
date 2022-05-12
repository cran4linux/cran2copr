%global __brp_check_rpaths %{nil}
%global packname  camtrapR
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Camera Trap Data Management and Preparation of Occupancy and Spatial Capture-Recapture Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         perl(Image::ExifTool)
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-overlap 
BuildRequires:    R-CRAN-secr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-overlap 
Requires:         R-CRAN-secr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-ggplot2 

%description
Management of and data extraction from camera trap data in wildlife
studies. The package provides a workflow for storing and sorting camera
trap photos (and videos), tabulates records of species and individuals,
and creates detection/non-detection matrices for occupancy and spatial
capture-recapture analyses with great flexibility. In addition, it can
visualise species activity data and provides simple mapping functions with
GIS export.

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
