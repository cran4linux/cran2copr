%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SFM
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Package for Analyzing Skew Factor Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-SOPC 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-SOPC 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-sn 
Requires:         R-stats 
Requires:         R-CRAN-psych 

%description
Generates Skew Factor Models data and applies Sparse Online Principal
Component (SOPC), Incremental Principal Component (IPC), Projected
Principal Component (PPC), Perturbation Principal Component (PPC),
Stochastic Approximation Principal Component (SAPC), Sparse Principal
Component (SPC) and other PC methods to estimate model parameters. It
includes capabilities for calculating mean squared error, relative error,
and sparsity of the loading matrix.The philosophy of the package is
described in Guo G. (2023) <doi:10.1007/s00180-022-01270-z>.

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
