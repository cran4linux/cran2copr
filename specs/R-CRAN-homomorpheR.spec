%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  homomorpheR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Homomorphic Computations in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-openfhe.R 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sodium 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-openfhe.R 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sodium 

%description
Privacy-preserving statistics across sites that never share their data,
using fully homomorphic encryption through the 'openfhe.R' interface to
OpenFHE (CKKS, BFV, BGV), with n-of-n threshold key generation so that no
single party can decrypt. Ships master/worker primitives that let ordinary
R modeling code run across sites, and a frozen implementation of the
Paillier additive scheme kept for backward compatibility.

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
