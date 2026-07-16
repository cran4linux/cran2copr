%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kro.inv.test
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Kronecker-Invariant Tests for High-Dimensional Separability Testing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RMTstat 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-covKCD 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
Requires:         R-CRAN-RMTstat 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-covKCD 
Requires:         R-CRAN-pracma 
Requires:         R-stats 

%description
Kronecker-invariant tests for high-dimensional separability testing of
matrix-variate data, focusing on Gaussian populations as benchmark cases.
Tests whether the population covariance matrix is represented as a
Kronecker product of row and column covariance matrices. Implements the
tests based on the eigenvalues of the sample core whose test statistics
are invariant to the separable component of the population covariance
matrix, referred to as Kronecker-invariance. Tests constructed using the
largest eigenvalue and the separable expansion of the sample core and
applying the extended likelihood ratio test for sphericity testing to the
sample core. For details, see Sung and Hoff (2025)
<doi:10.48550/arXiv.2506.17463>.

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
