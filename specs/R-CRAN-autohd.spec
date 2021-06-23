%global __brp_check_rpaths %{nil}
%global packname  autohd
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          High Dimensional Bayesian Survival Mediation Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-hdbm 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-ICBayes 
BuildRequires:    R-CRAN-icenReg 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-SurvRegCensCov 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-schoolmath 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-coxme 
BuildRequires:    R-CRAN-mlr3 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-hdbm 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-ICBayes 
Requires:         R-CRAN-icenReg 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-SurvRegCensCov 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-schoolmath 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-coxme 
Requires:         R-CRAN-mlr3 

%description
Perform mediation analysis for time to event high-dimensional data.
Mediation Analysis proposed by Miocevic et al.(2017)
<doi:10.1080/10705511.2017.1342541> as a statistical tool in the Bayesian
framework. Time to event data analysis methods like Cox proportional
hazard model, accelerated failure time model to work with high dimensional
data with Bayesian approaches are provided. Missing data imputation
techniques tool to work with high dimensional data coupled for mediation
analysis by presented by the active mediator variables.

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
