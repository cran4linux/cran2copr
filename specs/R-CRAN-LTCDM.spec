%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LTCDM
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Transition Cognitive Diagnosis Model with Covariates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GDINA 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggsignif 
Requires:         R-CRAN-GDINA 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggsignif 

%description
Implementation of the three-step approach of (latent transition) cognitive
diagnosis model (CDM) with covariates. This approach can be used for
single time-point situations (cross-sectional data) and multiple
time-point situations (longitudinal data) to investigate how the
covariates are associated with attribute mastery. For multiple time-point
situations, the three-step approach of latent transition CDM with
covariates allows researchers to assess changes in attribute mastery
status and to evaluate the covariate effects on both the initial states
and transition probabilities over time using latent logistic regression.
Because stepwise approaches often yield biased estimates, correction for
classification error probabilities (CEPs) is considered in this approach.
The three-step approach for latent transition CDM with covariates involves
the following steps: (1) fitting a CDM to the response data without
covariates at each time point separately, (2) assigning examinees to
latent states at each time point and computing the associated CEPs, and
(3) estimating the latent transition CDM with the known CEPs and computing
the regression coefficients. The method was proposed in Liang et al.
(2023) <doi:10.3102/10769986231163320> and demonstrated using mental
health data in Liang et al. (in press; annotated R code and data utilized
in this example are available in Mendeley data)
<doi:10.17632/kpjp3gnwbt.1>.

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
