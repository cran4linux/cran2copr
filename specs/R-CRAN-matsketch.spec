%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  matsketch
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Randomized Matrix Computations from Few Entries and Products

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Implements recent randomized algorithms that answer questions about a
large positive-semidefinite matrix while touching only a small part of it.
Randomly pivoted Cholesky builds a low-rank approximation from a few rows
of a kernel matrix (Chen, Epperly, Tropp and Webber (2025)
<doi:10.1002/cpa.22234>), with an accelerated variant based on rejection
sampling (Epperly, Tropp and Webber (2025) <doi:10.1137/24m1699048>). The
XTrace, XNysTrace and XDiag estimators recover the trace and diagonal of a
matrix that is available only through matrix-vector products (Epperly,
Tropp and Webber (2024) <doi:10.1137/23m1548323>), alongside the Hutch++
estimator of Meyer, Musco, Musco and Woodruff (2021)
<doi:10.1137/1.9781611976496.16>. Randomized Nystrom preconditioning
speeds up the conjugate gradient method for regularized linear systems
(Frangella, Tropp and Udell (2023) <doi:10.1137/21m1466244>). These pieces
are combined to fit restricted maximum likelihood variance-component
models on genomic relationship matrices without forming or factorizing the
covariance matrix.

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
