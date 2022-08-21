%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oro.pet
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Rigorous - Positron Emission Tomography

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-oro.dicom >= 0.4.0
BuildRequires:    R-CRAN-oro.nifti >= 0.4.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-msm 
Requires:         R-CRAN-oro.dicom >= 0.4.0
Requires:         R-CRAN-oro.nifti >= 0.4.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-msm 

%description
Image analysis techniques for positron emission tomography (PET) that form
part of the Rigorous Analytics bundle.

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
