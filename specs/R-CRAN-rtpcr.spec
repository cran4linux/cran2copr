%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rtpcr
%global packver   2.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          qPCR Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggsignif 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-emmeans 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggsignif 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-grid 
Requires:         R-CRAN-emmeans 

%description
Tools for qPCR data analysis using Delta Ct and Delta Delta Ct methods,
including t-test, Wilcoxon-test, ANOVA models, and publication-ready
visualizations. The package supports multiple target, and multiple
reference genes, and uses a calculation framework adopted from Ganger et
al. (2017) <doi:10.1186/s12859-017-1949-5> and Taylor et al. (2019)
<doi:10.1016/j.tibtech.2018.12.002>, covering both the Livak and Pfaffl
methods.

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
