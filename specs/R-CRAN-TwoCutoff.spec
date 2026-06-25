%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TwoCutoff
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Deriving Clinically Interpretable Cutoffs for Disease Biomarkers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mixtools 
Requires:         R-stats 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-gridExtra 

%description
Provides a reproducible pipeline for deriving two clinically meaningful
cutoffs for disease biomarkers using a unified two-stage framework. The
package integrates finite mixture modeling with risk prediction using
biomarker plus clinical features, followed by decision curve analysis to
evaluate clinical utility. Outputs include biomarker density plots, risk
calibration curves, decision curves, and summary tables of diagnostic
performance. Designed for researchers in bio-statistics, neurology, and
data science, this package emphasizes reproducibility, transparency, and
clear clinical relevance.

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
