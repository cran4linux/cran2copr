%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nmw
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Understanding Nonlinear Mixed Effects Modeling for Population Pharmacokinetics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MASS 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
This shows how 'NONMEM' (Beal SL, Sheiner LB, Boeckmann AJ, Bauer RJ.
NONMEM 7.5 Users Guides.  Icon plc, 2020) software works. 'NONMEM'
classical estimation methods such as 'First Order (FO) approximation',
'First Order Conditional Estimation (FOCE)', and 'Laplacian approximation'
are explained.  Functions are also provided for post-run processing of
NONMEM output files, generating PDF diagnostic reports including objective
function value analysis, parameter estimates, prediction and residual
diagnostics, empirical Bayes estimate (EBE) analysis, input data summary,
and individual pharmacokinetic parameter distributions.  Helper utilities
for building NONMEM-ready datasets from SDTM-style source tables are also
included.

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
