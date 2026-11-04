%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stagelife
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Random Number Generation and Inferences for Two-Stage Life-Testing Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lamW 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-lamW 
Requires:         R-parallel 
Requires:         R-stats 

%description
Provides random number generation, estimation, and hypothesis testing for
two-stage life-testing experiments in which units begin on a baseline
stress and, at a fixed or random change point, some or all surviving units
move to an elevated stress ("stage life testing"), following the
cumulative-exposure model of Laumen and Cramer (2019), "Stage life
testing", <doi:10.1002/nav.21874>. Twelve baseline lifetime distributions
are supplied (Weibull, Power Lindley, Exponentiated Lindley, Exponentiated
Exponential, Marshall-Olkin Exponential, Lomax, Exponentiated Teissier,
Log-Logistic, Chen, Log-normal, Gamma, and Power Muth/Power Teissier)
together with three parameter-sharing cases (common, shape1, shape11). The
package implements data simulation under both the fixed-proportion (typeP)
and fixed-count (typeM) rules and the simple-step-stress special case,
maximum likelihood estimation using a hybrid Nelder-Mead and BFGS
optimisation routine, asymptotic (Wald) and non-parametric/parametric
bootstrap confidence intervals (including log-scale variants that
guarantee a positive interval), a stage-1-observation planning
probability, Kolmogorov-Smirnov goodness-of-fit testing with a
parametric-bootstrap correction for estimated parameters, likelihood-ratio
and information criteria for nested/non-nested model comparison, and
diagnostic plots comparing fitted and empirical distributions, including
the cumulative distribution function (CDF), survival function,
probability-probability (P-P), and quantile-quantile (Q-Q) plots.

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
