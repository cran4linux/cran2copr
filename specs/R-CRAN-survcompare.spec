%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survcompare
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nested Cross-Validation to Compare Cox-PH, Cox-Lasso, Survival Random Forests

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 3.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-timeROC 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-randomForestSRC 
Requires:         R-CRAN-survival >= 3.0
Requires:         R-stats 
Requires:         R-CRAN-timeROC 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-randomForestSRC 

%description
Performs repeated nested cross-validation for Cox Proportionate Hazards,
Cox Lasso, Survival Random Forest, and their ensemble. Returns internally
validated concordance index, time-dependent area under the curve, Brier
score, calibration slope, and statistical testing of non-linear ensemble
outperforming the baseline Cox model. In this, it helps researchers to
quantify the gain of using a more complex survival model, or justify its
redundancy. Equally, it shows the performance value of the non-linear and
interaction terms, and may highlight the need of further feature
transformation. Further details can be found in Shamsutdinova, Stamate,
Roberts, & Stahl (2022) "Combining Cox Model and Tree-Based Algorithms to
Boost Performance and Preserve Interpretability for Health Outcomes"
<doi:10.1007/978-3-031-08337-2_15>, where the method is described as
Ensemble 1.

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
