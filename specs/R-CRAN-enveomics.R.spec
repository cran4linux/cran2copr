%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  enveomics.R
%global packver   1.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10.0
Release:          1%{?dist}%{?buildtag}
Summary:          Various Utilities for Microbial Genomics and Metagenomics

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9
Requires:         R-core >= 2.9
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-investr 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-investr 

%description
A collection of functions for microbial ecology and other applications of
genomics and metagenomics. Companion package for the Enveomics Collection
(Rodriguez-R, L.M. and Konstantinidis, K.T., 2016
<DOI:10.7287/peerj.preprints.1900v1>).

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
