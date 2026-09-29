%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DeltaTools
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          DELTA Analytic Tools and Learning Curve Analysis

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rms >= 8.1.1
BuildRequires:    R-CRAN-caret >= 7.0.1
BuildRequires:    R-CRAN-glmnet >= 5.0
BuildRequires:    R-CRAN-MatchIt >= 4.7.2
BuildRequires:    R-CRAN-plotly >= 4.12.0
BuildRequires:    R-CRAN-ggplot2 >= 4.0.3
BuildRequires:    R-CRAN-sjPlot >= 2.9.0
BuildRequires:    R-CRAN-twang >= 2.6.2
BuildRequires:    R-CRAN-gbm >= 2.2.3
BuildRequires:    R-CRAN-ldbounds >= 2.0.2
BuildRequires:    R-CRAN-mgcv >= 1.9.4
BuildRequires:    R-CRAN-stringr >= 1.6.0
BuildRequires:    R-CRAN-minpack.lm >= 1.2.4
BuildRequires:    R-CRAN-dplyr >= 1.2.1
BuildRequires:    R-CRAN-pROC >= 1.19.0.1
BuildRequires:    R-CRAN-data.table >= 1.18.4
BuildRequires:    R-CRAN-broom >= 1.0.12
BuildRequires:    R-CRAN-ROCR >= 1.0.12
BuildRequires:    R-CRAN-DescTools >= 0.99.60
BuildRequires:    R-CRAN-lmtest >= 0.9.40
BuildRequires:    R-CRAN-ResourceSelection >= 0.3.6
BuildRequires:    R-CRAN-parameters >= 0.28.3
BuildRequires:    R-CRAN-tableone >= 0.13.2
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-rms >= 8.1.1
Requires:         R-CRAN-caret >= 7.0.1
Requires:         R-CRAN-glmnet >= 5.0
Requires:         R-CRAN-MatchIt >= 4.7.2
Requires:         R-CRAN-plotly >= 4.12.0
Requires:         R-CRAN-ggplot2 >= 4.0.3
Requires:         R-CRAN-sjPlot >= 2.9.0
Requires:         R-CRAN-twang >= 2.6.2
Requires:         R-CRAN-gbm >= 2.2.3
Requires:         R-CRAN-ldbounds >= 2.0.2
Requires:         R-CRAN-mgcv >= 1.9.4
Requires:         R-CRAN-stringr >= 1.6.0
Requires:         R-CRAN-minpack.lm >= 1.2.4
Requires:         R-CRAN-dplyr >= 1.2.1
Requires:         R-CRAN-pROC >= 1.19.0.1
Requires:         R-CRAN-data.table >= 1.18.4
Requires:         R-CRAN-broom >= 1.0.12
Requires:         R-CRAN-ROCR >= 1.0.12
Requires:         R-CRAN-DescTools >= 0.99.60
Requires:         R-CRAN-lmtest >= 0.9.40
Requires:         R-CRAN-ResourceSelection >= 0.3.6
Requires:         R-CRAN-parameters >= 0.28.3
Requires:         R-CRAN-tableone >= 0.13.2
Requires:         R-methods 
Requires:         R-stats 

%description
A collection of tools for researchers interested in carrying out
parametric estimation of learning curves and device effects based on the
publication by Ssemaganda et al. (2025) <doi:10.2147/MDER.S520191> with
modified versions of propensity score matching (PSM) and inverse
probability of treatment weighting (IPTW).

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
