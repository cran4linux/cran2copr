%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  agriReg
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linear and Nonlinear Regression for Agricultural Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-drc >= 3.0.1
BuildRequires:    R-CRAN-lme4 >= 1.1.35
BuildRequires:    R-CRAN-patchwork >= 1.1.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-drc >= 3.0.1
Requires:         R-CRAN-lme4 >= 1.1.35
Requires:         R-CRAN-patchwork >= 1.1.0
Requires:         R-stats 
Requires:         R-utils 

%description
Fit, compare, and visualise linear and nonlinear regression models
tailored to field-trial and dose-response agricultural data. Provides S3
classes for mixed-effects models (via 'lme4'), nonlinear growth curves
(logistic, 'Gompertz', asymptotic, linear-plateau, quadratic), and
four/five-parameter log-logistic dose-response models (via 'drc').
Includes automated starting-value heuristics, goodness-of-fit statistics,
residual diagnostics, and 'ggplot2'-based visualisation. Methods are based
on Bates and Watts (1988, ISBN:9780471816430), Ritz and others (2015)
<doi:10.1371/journal.pone.0146021>, and Bates and others (2015)
<doi:10.18637/jss.v067.i01>.

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
