%global __brp_check_rpaths %{nil}
%global packname  mand
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Analysis for Neuroimaging Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-msma 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-oro.dicom 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-msma 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-oro.dicom 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-caret 

%description
Several functions can be used to analyze neuroimaging data using
multivariate methods based on the 'msma' package. The functions used in
the book entitled "Multivariate Analysis for Neuroimaging Data" (2021,
ISBN-13: 978-0367255329) are contained. Please also see Kawaguchi et al.
(2017) <doi:10.1093/biostatistics/kxx011> and Kawaguchi (2019)
<DOI:10.5772/intechopen.80531>.

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
