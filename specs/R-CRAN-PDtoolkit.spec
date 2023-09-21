%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PDtoolkit
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Tools for PD Rating Model Development and Validation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-monobin 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rpart 
Requires:         R-CRAN-monobin 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rpart 

%description
The goal of this package is to cover the most common steps in probability
of default (PD) rating model development and validation. The main
procedures available are those that refer to univariate, bivariate,
multivariate analysis, calibration and validation. Along with accompanied
'monobin' and 'monobinShiny' packages, 'PDtoolkit' provides functions
which are suitable for different data transformation and modeling tasks
such as: imputations, monotonic binning of numeric risk factors, binning
of categorical risk factors, weights of evidence (WoE) and information
value (IV) calculations, WoE coding (replacement of risk factors
modalities with WoE values), risk factor clustering, area under curve
(AUC) calculation and others. Additionally, package provides set of
validation functions for testing homogeneity, heterogeneity,
discriminatory and predictive power of the model.

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
