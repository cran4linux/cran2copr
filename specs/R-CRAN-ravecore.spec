%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ravecore
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Core File Structures and Workflows for 'RAVE'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-filearray >= 0.2.0
BuildRequires:    R-CRAN-ravepipeline >= 0.0.2
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-bidsr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-ieegio 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-ravetools 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-threeBrain 
Requires:         R-CRAN-filearray >= 0.2.0
Requires:         R-CRAN-ravepipeline >= 0.0.2
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-bidsr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-ieegio 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-ravetools 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-threeBrain 

%description
Defines storage standard for Read, process, and analyze intracranial
electroencephalography and deep-brain stimulation in 'RAVE', a
reproducible framework for analysis and visualization of iEEG by Magnotti,
Wang, and Beauchamp, (2020, <doi:10.1016/j.neuroimage.2020.117341>).
Supports brain imaging data structure (BIDS)
<https://bids.neuroimaging.io> and native file structure to ingest signals
from 'Matlab' data files, hierarchical data format 5 (HDF5), European data
format (EDF), BrainVision core data format (BVCDF), or BlackRock
Microsystem (NEV/NSx); process images in Neuroimaging informatics
technology initiative (NIfTI) and 'FreeSurfer' formats, providing brain
imaging normalization to template brain, facilitating 'threeBrain' package
for comprehensive electrode localization via 'YAEL' (your advanced
electrode localizer) by Wang, Magnotti, Zhang, and Beauchamp (2023,
<doi:10.1523/ENEURO.0328-23.2023>).

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
