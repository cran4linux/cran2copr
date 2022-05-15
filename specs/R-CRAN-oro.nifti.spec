%global __brp_check_rpaths %{nil}
%global packname  oro.nifti
%global packver   0.11.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.1
Release:          1%{?dist}%{?buildtag}
Summary:          Rigorous - 'NIfTI' + 'ANALYZE' + 'AFNI' : Input / Output

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RNifti >= 0.9.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-splines 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-RNifti >= 0.9.0
Requires:         R-stats 
Requires:         R-CRAN-bitops 
Requires:         R-splines 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-abind 

%description
Functions for the input/output and visualization of medical imaging data
that follow either the 'ANALYZE', 'NIfTI' or 'AFNI' formats.  This package
is part of the Rigorous Analytics bundle.

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
