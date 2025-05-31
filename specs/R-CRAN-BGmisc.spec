%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BGmisc
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          An R Package for Extended Behavior Genetics Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-kinship2 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-methods 

%description
Provides functions for behavior genetics analysis, including variance
component model identification [Hunter et al. (2021)
<doi:10.1007/s10519-021-10055-x>], calculation of relatedness coefficients
using path-tracing methods [Wright (1922) <doi:10.1086/279872>; McArdle &
McDonald (1984) <doi:10.1111/j.2044-8317.1984.tb00802.x>], inference of
relatedness, pedigree conversion, and simulation of multi-generational
family data [Lyu et al. (2024) <doi:10.1101/2024.12.19.629449>]. For a
full overview, see [Garrison et al. (2024) <doi:10.21105/joss.06203>].

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
