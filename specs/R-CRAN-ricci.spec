%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ricci
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ricci Calculus

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-calculus 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-calculus 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 

%description
Provides a compact 'R' interface for performing tensor calculations. This
is achieved by allowing (upper and lower) index labeling of arrays and
making use of Ricci calculus conventions to implicitly trigger
contractions and diagonal subsetting. Explicit tensor operations, such as
addition, subtraction and multiplication of tensors via the standard
operators, raising and lowering indices, taking symmetric or antisymmetric
tensor parts, as well as the Kronecker product are available. Common
tensors like the Kronecker delta, Levi Civita epsilon, certain metric
tensors, the Christoffel symbols, the Riemann as well as Ricci tensors are
provided. The covariant derivative of tensor fields with respect to any
metric tensor can be evaluated. An effort was made to provide the user
with useful error messages.

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
