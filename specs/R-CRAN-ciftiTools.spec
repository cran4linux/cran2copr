%global __brp_check_rpaths %{nil}
%global packname  ciftiTools
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Reading and Visualizing CIFTI Brain Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gifti > 0.7.5
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-RNifti 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-gifti > 0.7.5
Requires:         R-CRAN-fields 
Requires:         R-grDevices 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-RNifti 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-xml2 

%description
CIFTI files contain brain imaging data in "gray-ordinates", which
represent the gray matter as cortical surface vertices (left and right)
and subcortical voxels (cerebellum, basal ganglia, and other deep gray
matter). 'ciftiTools' uses the Connectome Workbench to read CIFTI files
into R and apply common pre-processing steps (e.g. smoothing, resampling).
It also provides tools for visualizing the cortical surface with GIFTI
files, and for visualizing the subcortical volume.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
