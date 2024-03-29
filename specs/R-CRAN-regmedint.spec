%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  regmedint
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Regression-Based Causal Mediation Analysis with Interaction and Effect Modification Terms

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-survival 

%description
This is an extension of the regression-based causal mediation analysis
first proposed by Valeri and VanderWeele (2013) <doi:10.1037/a0031034> and
Valeri and VanderWeele (2015) <doi:10.1097/EDE.0000000000000253>). It
supports including effect measure modification by
covariates(treatment-covariate and mediator-covariate product terms in
mediator and outcome regression models) as proposed by Li et al (2023)
<doi:10.1097/EDE.0000000000001643>. It also accommodates the original
'SAS' macro and 'PROC CAUSALMED' procedure in 'SAS' when there is no
effect measure modification. Linear and logistic models are supported for
the mediator model. Linear, logistic, loglinear, Poisson, negative
binomial, Cox, and accelerated failure time (exponential and Weibull)
models are supported for the outcome model.

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
