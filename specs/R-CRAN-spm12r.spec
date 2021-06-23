%global __brp_check_rpaths %{nil}
%global packname  spm12r
%global packver   2.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          Wrapper Functions for 'SPM' (Statistical Parametric Mapping) Version 12 from the 'Wellcome' Trust Centre for 'Neuroimaging'

License:          GPL-2 | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-matlabr >= 1.5.2
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-neurobase 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-git2r 
Requires:         R-CRAN-matlabr >= 1.5.2
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-neurobase 
Requires:         R-utils 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-git2r 

%description
Installs 'SPM12' to the R library directory and has associated functions
for 'fMRI' and general imaging utilities, called through 'MATLAB'.

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
