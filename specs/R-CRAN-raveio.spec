%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  raveio
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          File-System Toolbox for RAVE Project

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 3.7.0
BuildRequires:    R-CRAN-R.matlab >= 3.6.2
BuildRequires:    R-CRAN-yaml >= 2.2.1
BuildRequires:    R-CRAN-remotes >= 2.1.2
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-hdf5r >= 1.3.4
BuildRequires:    R-CRAN-edfReader >= 1.2.1
BuildRequires:    R-CRAN-promises >= 1.2.0
BuildRequires:    R-CRAN-fst >= 0.9.2
BuildRequires:    R-CRAN-targets >= 0.8.0
BuildRequires:    R-CRAN-threeBrain >= 0.2.5
BuildRequires:    R-CRAN-filearray >= 0.1.3
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dipsaus 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-globals 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-callr >= 3.7.0
Requires:         R-CRAN-R.matlab >= 3.6.2
Requires:         R-CRAN-yaml >= 2.2.1
Requires:         R-CRAN-remotes >= 2.1.2
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-hdf5r >= 1.3.4
Requires:         R-CRAN-edfReader >= 1.2.1
Requires:         R-CRAN-promises >= 1.2.0
Requires:         R-CRAN-fst >= 0.9.2
Requires:         R-CRAN-targets >= 0.8.0
Requires:         R-CRAN-threeBrain >= 0.2.5
Requires:         R-CRAN-filearray >= 0.1.3
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dipsaus 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-globals 
Requires:         R-CRAN-R6 

%description
Includes multiple cross-platform read/write interfaces for 'RAVE' project.
'RAVE' stands for "R analysis and visualization of human intracranial
electroencephalography data". The whole project aims at providing powerful
free-source package that analyze brain recordings from patients with
electrodes placed on the cortical surface or inserted into the brain.
'raveio' as part of this project provides tools to read/write
neurophysiology data from/to 'RAVE' file structure, as well as several
popular formats including 'EDF(+)', 'Matlab', 'BIDS-iEEG', and 'HDF5',
etc. Documentation and examples about 'RAVE' project are provided at
<https://openwetware.org/wiki/RAVE>, and the paper by John F. Magnotti,
Zhengjia Wang, Michael S. Beauchamp (2020)
<doi:10.1016/j.neuroimage.2020.117341>; see 'citation("raveio")' for
details.

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
