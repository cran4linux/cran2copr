%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MoPlot
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualize and Interpret Contrasts in Regression Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-effectsize 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-parameters 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-reformulas 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-effectsize 
Requires:         R-CRAN-glmmTMB 
Requires:         R-grid 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-parameters 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-reformulas 
Requires:         R-CRAN-tibble 

%description
Visualizes and interprets the contrasts used to code categorical
predictors in fitted regression models. Each coefficient is translated
into the comparison between the levels, or groups of levels, that it
estimates, derived from the hypothesis matrix of the contrast coding, and
is displayed together with the coefficient, its confidence interval, and
an approximate effect size. Interactions among categorical predictors are
decomposed into differences of differences. Supports models fitted with
'stats', 'lme4', 'lmerTest', 'nlme', and 'glmmTMB'.

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
