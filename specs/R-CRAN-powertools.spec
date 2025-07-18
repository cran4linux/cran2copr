%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  powertools
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Power and Sample Size Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-PowerTOST 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-PowerTOST 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 
Requires:         R-CRAN-knitr 

%description
Power and sample size calculations for a variety of study designs and
outcomes. Methods include t tests, ANOVA (including tests for
interactions, simple effects and contrasts), proportions, categorical data
(chi-square tests and proportional odds), linear, logistic and Poisson
regression, alternative and coprimary endpoints, power for confidence
intervals, correlation coefficient tests, cluster randomized trials,
individually randomized group treatment trials, multisite trials,
treatment-by-covariate interaction effects and nonparametric tests of
location. Utilities are provided for computing various effect sizes.
Companion package to the book "Power and Sample Size in R", Crespi (2025,
ISBN:9781138591622). Further resources available at
<https://powerandsamplesize.org/>.

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
