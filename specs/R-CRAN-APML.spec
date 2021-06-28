%global __brp_check_rpaths %{nil}
%global packname  APML
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          An Approach for Machine-Learning Modelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-h2o 
BuildRequires:    R-CRAN-performanceEstimation 
BuildRequires:    R-CRAN-dummies 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-h2o 
Requires:         R-CRAN-performanceEstimation 
Requires:         R-CRAN-dummies 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-survival 

%description
We include 1) data cleaning including variable scaling, missing values and
unbalanced variables identification and removing, and strategies for
variable balance improving; 2) modeling based on random forest and
gradient boosted model including feature selection, model training,
cross-validation and external testing. For more information, please see
Deng X (2021). <doi:10.1016/j.scitotenv.2020.144746>; H2O.ai (Oct. 2016).
R Interface for H2O, R package version 3.10.0.8.
<https://github.com/h2oai/h2o-3>; Zhang W (2016).
<doi:10.1016/j.scitotenv.2016.02.023>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
