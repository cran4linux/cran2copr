%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  osirad
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          PET Voxels and Radiomics from 'OsiriX' Regions of Interest

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-oro.dicom 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xml2 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-oro.dicom 
Requires:         R-stats 
Requires:         R-CRAN-xml2 

%description
Reads regions of interest (ROIs) drawn in the 'OsiriX' medical image
viewer and exported as XML files, and recovers the exact voxels of each
ROI on the positron emission tomography (PET) series stored as Digital
Imaging and Communications in Medicine (DICOM) files. The voxels are found
by matching the voxel values stored in the XML file to the standardised
uptake values (SUV) computed from the DICOM header. The resulting voxel
table (positions in pixels and millimetres, and SUV) can be passed to the
'Python' library 'PyRadiomics' (van Griethuysen et al. (2017)
<doi:10.1158/0008-5472.CAN-17-0339>) through 'reticulate' to compute
radiomics features.

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
