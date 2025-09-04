%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multiModTest
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Information Assessment for Individual Modalities in Multimodal Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-SIS 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-MBESS 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-SIS 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-MBESS 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-dplyr 

%description
Provides methods for quantifying the information gain contributed by
individual modalities in multimodal regression models. Information gain is
measured using Expected Relative Entropy (ERE) or pseudo-R² metrics, with
corresponding p-values and confidence intervals. Currently supports linear
and logistic regression models with plans for extension to additional
Generalized Linear Models and Cox proportional hazard model.

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
