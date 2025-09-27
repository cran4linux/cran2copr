%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SIMPLE.REGRESSION
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          OLS, Moderated, Logistic, and Count Regressions Made Simple

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-pscl 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-pscl 

%description
Provides SPSS- and SAS-like output for least squares multiple regression,
logistic regression, and count variable regressions. Detailed output is
also provided for OLS moderated regression, interaction plots, and
Johnson-Neyman regions of significance. The output includes standardized
coefficients, partial and semi-partial correlations, collinearity
diagnostics, plots of residuals, and detailed information about simple
slopes for interactions. The output for some functions includes Bayes
Factors and, if requested, regression coefficients from Bayesian Markov
Chain Monte Carlo analyses. There are numerous options for model plots.
The REGIONS_OF_SIGNIFICANCE function also provides Johnson-Neyman regions
of significance and plots of interactions for both lm and lme models.
There is also a function for partial and semipartial correlations and a
function for conducting Cohen's set correlation analyses.

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
