%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fslr
%global packver   2.27.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.27.0
Release:          1%{?dist}%{?buildtag}
Summary:          Wrapper Functions for 'FSL' ('FMRIB' Software Library) from Functional MRI of the Brain ('FMRIB')

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-neurobase >= 1.32.0
BuildRequires:    R-CRAN-oro.nifti >= 0.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-neurobase >= 1.32.0
Requires:         R-CRAN-oro.nifti >= 0.5.0
Requires:         R-methods 
Requires:         R-CRAN-R.utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Wrapper functions that interface with 'FSL'
<http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/>, a powerful and commonly-used
'neuroimaging' software, using system commands. The goal is to be able to
interface with 'FSL' completely in R, where you pass R objects of class
'nifti', implemented by package 'oro.nifti', and the function executes an
'FSL' command and returns an R object of class 'nifti' if desired.

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
