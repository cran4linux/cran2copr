%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WMAP
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted Meta-Analysis with Pseudo-Populations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pkgcond 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-zeallot 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-pkgcond 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-zeallot 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-forcats 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Implementation of integrative weighting approaches for multiple
observational studies and causal inferences. The package features three
weighting approaches, each representing a special case of the unified
weighting framework, introduced by Guha and Li (2024)
<doi:10.1093/biomtc/ujae070>, which includes an extension of inverse
probability weights for data integration settings.

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
