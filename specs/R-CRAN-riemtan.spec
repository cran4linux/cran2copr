%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  riemtan
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Riemannian Metrics for Symmetric Positive Definite Matrices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-furrr 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-furrr 

%description
Implements various Riemannian metrics for symmetric positive definite
matrices, including AIRM (Affine Invariant Riemannian Metric, see Pennec,
Fillard, and Ayache (2006) <doi:10.1007/s11263-005-3222-z>), Log-Euclidean
(see Arsigny, Fillard, Pennec, and Ayache (2006) <doi:10.1002/mrm.20965>),
Euclidean, Log-Cholesky (see Lin (2019) <doi:10.1137/18M1221084>), and
Bures-Wasserstein metrics (see Bhatia, Jain, and Lim (2019)
<doi:10.1016/j.exmath.2018.01.002>). Provides functions for computing
logarithmic and exponential maps, vectorization, and statistical
operations on the manifold of positive definite matrices.

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
