%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BioPred
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          An R Package for Biomarkers Analysis in Precision Medicine

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-PropCIs 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-onewaytests 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-PropCIs 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-onewaytests 
Requires:         R-CRAN-car 

%description
Provides functions for training extreme gradient boosting model using
propensity score A-learning and weight-learning methods. For further
details, see Liu et al. (2024) <doi:10.1093/bioinformatics/btae592>.

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
