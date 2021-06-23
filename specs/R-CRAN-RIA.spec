%global __brp_check_rpaths %{nil}
%global packname  RIA
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Radiomics Image Analysis Toolbox for Medial Images

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nat >= 1.8.11
BuildRequires:    R-CRAN-oro.nifti >= 0.9.1
BuildRequires:    R-CRAN-oro.dicom >= 0.5.0
Requires:         R-CRAN-nat >= 1.8.11
Requires:         R-CRAN-oro.nifti >= 0.9.1
Requires:         R-CRAN-oro.dicom >= 0.5.0

%description
Radiomics image analysis toolbox for 2D and 3D radiological images. RIA
supports DICOM, NIfTI and nrrd file formats. RIA calculates first-order,
gray level co-occurrence matrix, gray level run length matrix and
geometry-based statistics. Almost all calculations are done using
vectorized formulas to optimize run speeds. Calculation of several
thousands of parameters only takes minutes on a single core of a
conventional PC.

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
