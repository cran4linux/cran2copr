%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  riskutility
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Disclosure Risk and Data Utility Metrics for Synthetic and Anonymized Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-VIM 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-VIM 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Provides comprehensive methods to measure disclosure risk and data utility
for anonymized and synthetic data. Implements attribution-based risk
metrics including Correct Attribution Probability (CAP), Targeted CAP
(TCAP), Within Equivalence Class Attribution Probability (WEAP), and RAPID
(Risk of Attribute Prediction-Induced Disclosure). Also provides
distance-based privacy metrics such as Distance to Closest Record (DCR),
Nearest Neighbor Distance Ratio (NNDR), and Identical Match Share (IMS).
Utility assessment includes propensity score analysis, distribution
comparisons, and various statistical tests. Methods are based on Taub et
al. (2018) <doi:10.1007/978-3-319-99771-1_9> and related literature.
Designed for integration with 'simPop' S4 classes.

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
