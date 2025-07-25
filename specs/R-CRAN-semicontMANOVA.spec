%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  semicontMANOVA
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate ANalysis of VAriance with Ridge Regularization for Semicontinuous High-Dimensional Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-mvtnorm 

%description
Implements Multivariate ANalysis Of VAriance (MANOVA) parameters'
inference and test with regularization for semicontinuous high-dimensional
data. The method can be applied also in presence of low-dimensional data.
The p-value can be obtained through asymptotic distribution or using a
permutation procedure. The package gives also the possibility to simulate
this type of data. Method is described in Elena Sabbioni, Claudio
Agostinelli and Alessio Farcomeni (2025) A regularized MANOVA test for
semicontinuous high-dimensional data. Biometrical Journal, 67:e70054. DOI
<doi:10.1002/bimj.70054>, arXiv DOI <doi:10.48550/arXiv.2401.04036>.

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
