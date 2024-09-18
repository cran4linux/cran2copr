%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DEXiR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          'DEXi' Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-graphics 

%description
A software package for using 'DEXi' models. 'DEXi' models are hierarchical
qualitative multi-criteria decision models developed according to the
method DEX (Decision EXpert,
<https://dex.ijs.si/documentation/DEX_Method/DEX_Method.html>), using the
program 'DEXi' (<https://kt.ijs.si/MarkoBohanec/dexi.html>) or 'DEXiWin'
(<https://dex.ijs.si/dexisuite/dexiwin.html>). A typical workflow with
'DEXiR' consists of: (1) reading a '.dxi' file, previously made using the
'DEXi' software (function read_dexi()), (2) making a data frame containing
input values of one or more decision alternatives, (3) evaluating those
alternatives (function evaluate()), (4) analyzing alternatives
(selective_explanation(), plus_minus(), compare_alternatives()), (5)
drawing charts. 'DEXiR' is restricted to using models produced externally
by the 'DEXi' software and does not provide functionality for creating
and/or editing 'DEXi' models directly in 'R'.

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
