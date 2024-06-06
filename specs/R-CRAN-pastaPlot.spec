%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pastaPlot
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spaghetti-Plot Fixed and Random Effects of Linear Mixed Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggeffects 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-ggeffects 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmmTMB 
Requires:         R-CRAN-lme4 

%description
Plot both fixed and random effects of linear mixed models, multilevel
models in a single spaghetti plot. The package allows to visualize the
effect of a predictor on a criterion between different levels of a
grouping variable. Additionally, confidence intervals can be displayed for
fixed effects. Calculation of predicted values of random effects allows
only models with one random intercept and/or one random slope to be
plotted. Confidence intervals and predicted values of fixed effects are
computed using the 'ggpredict' function from the 'ggeffects' package.
Lüdecke, D. (2018) <doi:10.21105/joss.00638>.

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
