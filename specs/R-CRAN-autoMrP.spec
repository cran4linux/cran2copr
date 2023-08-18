%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autoMrP
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Improving MrP with Ensemble Learning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-gbm >= 2.1.5
BuildRequires:    R-CRAN-doRNG >= 1.8.2
BuildRequires:    R-CRAN-e1071 >= 1.7.3
BuildRequires:    R-CRAN-glmmLasso >= 1.5.1
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-knitr >= 1.29
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-lme4 >= 1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-CRAN-EBMAforecast >= 1.0.0
BuildRequires:    R-CRAN-forcats >= 0.5.1
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-gbm >= 2.1.5
Requires:         R-CRAN-doRNG >= 1.8.2
Requires:         R-CRAN-e1071 >= 1.7.3
Requires:         R-CRAN-glmmLasso >= 1.5.1
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-knitr >= 1.29
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-lme4 >= 1.1
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-CRAN-EBMAforecast >= 1.0.0
Requires:         R-CRAN-forcats >= 0.5.1
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-purrr >= 0.3.4

%description
A tool that improves the prediction performance of multilevel regression
with post-stratification (MrP) by combining a number of machine learning
methods. For information on the method, please refer to Broniecki, Wüest,
Leemann (2020) ''Improving Multilevel Regression with Post-Stratification
Through Machine Learning (autoMrP)'' forthcoming in 'Journal of Politics'.
Final pre-print version:
<https://lucasleemann.files.wordpress.com/2020/07/automrp-r2pa.pdf>.

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
