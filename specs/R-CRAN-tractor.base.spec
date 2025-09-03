%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tractor.base
%global packver   3.4.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Read, Manipulate and Visualise Magnetic Resonance Images

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ore >= 1.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reportr 
BuildRequires:    R-CRAN-shades 
BuildRequires:    R-CRAN-RNifti 
Requires:         R-CRAN-ore >= 1.3.0
Requires:         R-methods 
Requires:         R-CRAN-reportr 
Requires:         R-CRAN-shades 
Requires:         R-CRAN-RNifti 

%description
Functions for working with magnetic resonance images. Reading and writing
of popular file formats (DICOM, Analyze, NIfTI-1, NIfTI-2, MGH);
interactive and non-interactive visualisation; flexible image
manipulation; metadata and sparse image handling.

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
