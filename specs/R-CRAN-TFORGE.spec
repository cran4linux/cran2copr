%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TFORGE
%global packver   0.1.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.14
Release:          1%{?dist}%{?buildtag}
Summary:          Tests for Geophysical Eigenvalues

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rdpack 

%description
The eigenvalues of observed symmetric matrices are often of intense
scientific interest. This package offers single sample tests for the
eigenvalues of the population mean or the eigenvalue-multiplicity of the
population mean. For k-samples, this package offers tests for equal
eigenvalues between samples. Included is support for matrices with
constraints common to geophysical tensors (constant trace, sum of squared
eigenvalues, or both) and eigenvectors are usually considered nuisance
parameters. Pivotal bootstrap methods enable these tests to have good
performance for small samples (n=15 for 3x3 matrices). These methods were
developed and studied by Hingee, Scealy and Wood (2026, "Nonparametric
bootstrap inference for the eigenvalues of geophysical tensors", accepted
by the Journal of American Statistical Association). Also available is a
2-sample test using a Gaussian orthogonal ensemble approximation and an
eigenvalue-multiplicity test that assumes orthogonally-invariant
covariance.

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
