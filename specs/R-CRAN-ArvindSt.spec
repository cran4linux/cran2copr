%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ArvindSt
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Five Novel Stochastic Regression Models with Arvind-Distributed Errors and Effects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-tvReg 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-tvReg 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 

%description
Implements the 'Arvind' distribution and five novel stochastic regression
models that replace the traditional Gaussian error assumption with
'Arvind'-distributed errors. The 'Arvind' distribution is a flexible
single-parameter continuous distribution on the positive real line
characterised by a polynomial numerator with Gaussian-type decay. The
package provides complete distribution functions (darvind(), parvind(),
qarvind(), rarvind()), maximum likelihood estimation via fit_arvind_mle(),
and five model-fitting routines: Random Walk on Coefficients via
fit_rw1(), Time-Varying Coefficient Linear Model via fit_tvlm(),
Simulation-Extrapolation via fit_simex(), Mixed-Effects Regression via
fit_mixed(), and Regime-Switching Hidden Markov Model via fit_hmm().
Additionally provides Monte Carlo forecasting with prediction intervals
via forecast_arvind(), comprehensive goodness-of-fit diagnostics (21
metrics and 25 plots) via diagnostics_arvind() and plot_arvind(), k-fold
and rolling-window cross-validation via cv_arvind(), and unified model
comparison via summary_arvind(). For more details see Pandey, Singh,
Tyagi, and Tyagi (2024), "Modelling climate, COVID-19, and reliability
data: A new continuous lifetime model under different methods of
estimation", 'Statistics and Applications', 22(2).

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
