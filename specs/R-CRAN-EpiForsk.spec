%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EpiForsk
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Code Sharing at the Department of Epidemiology Research at Statens Serum Institut

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-grf 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-policytree 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-svyVGAM 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-grf 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-MatchIt 
Requires:         R-methods 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-policytree 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-svyVGAM 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-VGAM 

%description
This is a collection of assorted functions and examples collected from
various projects. Currently we have functionalities for simplifying
overlapping time intervals, Charlson comorbidity score constructors for
Danish data, getting frequency for multiple variables, getting
standardized output from logistic and log-linear regressions, sibling
design linear regression functionalities a method for calculating the
confidence intervals for functions of parameters from a GLM, Bayes
equivalent for hypothesis testing with asymptotic Bayes factor, and
several help functions for generalized random forest analysis using 'grf'.

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
