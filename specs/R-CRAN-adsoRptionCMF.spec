%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adsoRptionCMF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Classical Model Fitting of Adsorption Isotherms

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nls2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-boot 
Requires:         R-CRAN-nls2 
Requires:         R-stats 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-boot 

%description
Provides tools for classical parameter estimation of adsorption isotherm
models, including both linear and nonlinear forms of the Freundlich,
Langmuir, and Temkin isotherms. This package allows users to fit these
models to experimental data, providing parameter estimates along with fit
statistics such as Akaike Information Criterion (AIC) and Bayesian
Information Criterion (BIC). Error metrics are computed to evaluate model
performance, and the package produces model fit plots with bootstrapped
95%% confidence intervals. Additionally, it generates residual plots for
diagnostic assessment of the models. Researchers and engineers in material
science, environmental engineering, and chemical engineering can
rigorously analyze adsorption behavior in their systems using this
straightforward, non-Bayesian approach. For more details, see Harding
(1907) <doi:10.2307/2987516>.

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
