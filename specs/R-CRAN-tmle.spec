%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tmle
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Targeted Maximum Likelihood Estimation

License:          BSD_3_clause + file LICENSE | GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-SuperLearner >= 2.0
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-SuperLearner >= 2.0
Requires:         R-CRAN-glmnet 

%description
Targeted maximum likelihood estimation of point treatment effects
(Targeted Maximum Likelihood Learning, The International Journal of
Biostatistics, 2(1), 2006.  This version automatically estimates the
additive treatment effect among the treated (ATT) and among the controls
(ATC).  The tmle() function calculates the adjusted marginal difference in
mean outcome associated with a binary point treatment, for continuous or
binary outcomes.  Relative risk and odds ratio estimates are also reported
for binary outcomes. Missingness in the outcome is allowed, but not in
treatment assignment or baseline covariate values.  The population mean is
calculated when there is missingness, and no variation in the treatment
assignment. The tmleMSM() function estimates the parameters of a marginal
structural model for a binary point treatment effect. Effect estimation
stratified by a binary mediating variable is also available. An ID
argument can be used to identify repeated measures. Default settings call
'SuperLearner' to estimate the Q and g portions of the likelihood, unless
values or a user-supplied regression function are passed in as arguments.

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
