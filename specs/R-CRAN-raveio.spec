%global __brp_check_rpaths %{nil}
%global packname  raveio
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Utility Toolbox for RAVE Project

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.matlab >= 3.6.2
BuildRequires:    R-CRAN-yaml >= 2.2.1
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-edfReader >= 1.2.1
BuildRequires:    R-CRAN-fst >= 0.9.2
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-ini >= 0.3.1
BuildRequires:    R-CRAN-dipsaus >= 0.0.9
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-BiocManager 
Requires:         R-CRAN-R.matlab >= 3.6.2
Requires:         R-CRAN-yaml >= 2.2.1
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-edfReader >= 1.2.1
Requires:         R-CRAN-fst >= 0.9.2
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-ini >= 0.3.1
Requires:         R-CRAN-dipsaus >= 0.0.9
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-parallel 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-later 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-BiocManager 

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
