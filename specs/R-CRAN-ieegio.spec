%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ieegio
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          File IO for Intracranial Electroencephalography

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R.matlab >= 3.7.0
BuildRequires:    R-CRAN-data.table >= 1.16.0
BuildRequires:    R-CRAN-fst >= 0.9.0
BuildRequires:    R-CRAN-gifti >= 0.8.0
BuildRequires:    R-CRAN-filearray >= 0.1.8
BuildRequires:    R-CRAN-readNSx >= 0.0.5
BuildRequires:    R-CRAN-rpyANTs >= 0.0.3
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-fastmap 
BuildRequires:    R-CRAN-freesurferformats 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-hdf5r 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-R.matlab >= 3.7.0
Requires:         R-CRAN-data.table >= 1.16.0
Requires:         R-CRAN-fst >= 0.9.0
Requires:         R-CRAN-gifti >= 0.8.0
Requires:         R-CRAN-filearray >= 0.1.8
Requires:         R-CRAN-readNSx >= 0.0.5
Requires:         R-CRAN-rpyANTs >= 0.0.3
Requires:         R-CRAN-digest 
Requires:         R-CRAN-fastmap 
Requires:         R-CRAN-freesurferformats 
Requires:         R-CRAN-fs 
Requires:         R-grDevices 
Requires:         R-CRAN-hdf5r 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
Integrated toolbox supporting common file formats used for intracranial
Electroencephalography (iEEG) and deep-brain stimulation (DBS) study.

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
