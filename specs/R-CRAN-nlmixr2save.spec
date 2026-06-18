%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nlmixr2save
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Save 'nlmixr2' Fits in a Format Readable Outside 'nlmixr2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rxode2 > 5.0.1
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-rxode2 > 5.0.1
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-zip 

%description
Provides tools to save 'nlmixr2' fitted models in a portable format
readable outside of 'nlmixr2' and independent of the package version.
'nlmixr2' fits and compares nonlinear mixed-effects models in differential
equations with flexible dosing information commonly seen in
pharmacokinetics and pharmacodynamics (Almquist, Leander, and Jirstrand
2015 <doi:10.1007/s10928-015-9409-1>). Differential equation solving uses
compiled C code from the 'rxode2' package (Wang, Hallow, and James 2015
<doi:10.1002/psp4.12052>).

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
