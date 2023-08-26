%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evalITR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluating Individualized Treatment Rules

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.0
BuildRequires:    R-CRAN-dplyr >= 1.0
BuildRequires:    R-CRAN-Matrix >= 1.0
BuildRequires:    R-CRAN-quadprog >= 1.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-ggdist 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-grf 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-rqPen 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-bartCause 
BuildRequires:    R-CRAN-SuperLearner 
Requires:         R-CRAN-MASS >= 7.0
Requires:         R-CRAN-dplyr >= 1.0
Requires:         R-CRAN-Matrix >= 1.0
Requires:         R-CRAN-quadprog >= 1.0
Requires:         R-stats 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-ggdist 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-grf 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-rqPen 
Requires:         R-CRAN-scales 
Requires:         R-utils 
Requires:         R-CRAN-bartCause 
Requires:         R-CRAN-SuperLearner 

%description
Provides various statistical methods for evaluating Individualized
Treatment Rules under randomized data. The provided metrics include
Population Average Value (PAV), Population Average Prescription Effect
(PAPE), Area Under Prescription Effect Curve (AUPEC). It also provides the
tools to analyze Individualized Treatment Rules under budget constraints.
Detailed reference in Imai and Li (2019) <arXiv:1905.05389>.

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
