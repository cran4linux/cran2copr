%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rTensor2
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          MultiLinear Algebra

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-wavethresh 
BuildRequires:    R-CRAN-gsignal 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-methods 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-wavethresh 
Requires:         R-CRAN-gsignal 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixcalc 

%description
A set of tools for basic tensor operators.  A tensor in the context of
data analysis in a multidimensional array. The tools in this package rely
on using any discrete transformation (e.g. Fast Fourier Transform (FFT)).
Standard tools included are the Eigenvalue decomposition of a tensor, the
QR decomposition and LU decomposition.  Other functionality includes the
inverse of a tensor and the transpose of a symmetric tensor. Functionality
in the package is outlined in Kernfeld et al. (2015)
<https://www.sciencedirect.com/science/article/pii/S0024379515004358>.

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
