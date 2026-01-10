%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mispitools
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Missing Person Identification Tools

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forrel 
BuildRequires:    R-CRAN-pedtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DirichletReg 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
Requires:         R-CRAN-forrel 
Requires:         R-CRAN-pedtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-patchwork 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DirichletReg 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 

%description
A comprehensive toolkit for missing person identification combining
genetic and non-genetic evidence within a Bayesian framework. Computes
likelihood ratios (LRs) for DNA profiles, biological sex, age, hair color,
and birthdate evidence. Provides decision analysis tools including optimal
LR thresholds, error rate calculations, and ROC curve visualization.
Includes interactive Shiny applications for exploring evidence
combinations. For methodological details see Marsico et al. (2023)
<doi:10.1016/j.fsigen.2023.102891> and Marsico, Vigeland et al. (2021)
<doi:10.1016/j.fsigen.2021.102519>.

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
