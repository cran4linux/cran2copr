%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EvalTest
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Evaluating Diagnostic Test Performance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.1
Requires:         R-core >= 4.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-binom 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-stats 
Requires:         R-CRAN-binom 

%description
Evaluates diagnostic test performance using data from laboratory or
diagnostic research. It includes functions to compute common performance
indicators along with their confidence intervals, and offers an
interactive 'shiny' application for comprehensive analysis including ROC
curve visualization and related metrics. It supports both binary and
continuous test variables. It allows users to compute key performance
indicators and visualize Receiver Operating Characteristic (ROC) curves,
determine optimal cut-off thresholds, display confusion matrix, and export
publication-ready plot. It aims to facilitate the application of
statistical methods in diagnostic test evaluation by healthcare
professionals. Methodological details and references for the computation
of performance indicators are provided in the package vignette.

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
