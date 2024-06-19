%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iNEXT.4steps
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Four-Step Biodiversity Analysis Based on 'iNEXT'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-iNEXT.3D 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-iNEXT.3D 

%description
Expands 'iNEXT' to include the estimation of sample completeness and
evenness. The package provides simple functions to perform the following
four-step biodiversity analysis: STEP 1: Assessment of sample completeness
profiles. STEP 2a: Analysis of size-based rarefaction and extrapolation
sampling curves to determine whether the asymptotic diversity can be
accurately estimated. STEP 2b: Comparison of the observed and the
estimated asymptotic diversity profiles. STEP 3: Analysis of
non-asymptotic coverage-based rarefaction and extrapolation sampling
curves. STEP 4: Assessment of evenness profiles. The analyses in STEPs 2a,
2b and STEP 3 are mainly based on the previous 'iNEXT' package. Refer to
the 'iNEXT' package for details. This package is mainly focusing on the
computation for STEPs 1 and 4. See Chao et al. (2020)
<doi:10.1111/1440-1703.12102> for statistical background.

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
