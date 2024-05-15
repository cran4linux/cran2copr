%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  freesurfer
%global packver   1.6.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.10
Release:          1%{?dist}%{?buildtag}
Summary:          Wrapper Functions for 'Freesurfer'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-neurobase 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-CRAN-neurobase 
Requires:         R-tools 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-reshape2 
Requires:         R-utils 

%description
Wrapper functions that interface with 'Freesurfer'
<https://surfer.nmr.mgh.harvard.edu/>, a powerful and commonly-used
'neuroimaging' software, using system commands. The goal is to be able to
interface with 'Freesurfer' completely in R, where you pass R objects of
class 'nifti', implemented by package 'oro.nifti', and the function
executes an 'Freesurfer' command and returns an R object of class 'nifti'
or necessary output.

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
