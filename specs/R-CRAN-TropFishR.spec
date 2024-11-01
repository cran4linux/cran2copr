%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TropFishR
%global packver   1.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tropical Fisheries Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-propagate 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-GA 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-propagate 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
A compilation of fish stock assessment methods for the analysis of
length-frequency data in the context of data-poor fisheries. Includes
methods and examples included in the FAO Manual by P. Sparre and S.C.
Venema (1998), "Introduction to tropical fish stock assessment"
(<https://openknowledge.fao.org/server/api/core/bitstreams/bc7c37b6-30df-49c0-b5b4-8367a872c97e/content>),
as well as other more recent methods.

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
