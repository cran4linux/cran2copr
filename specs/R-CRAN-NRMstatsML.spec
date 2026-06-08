%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NRMstatsML
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical and Machine Learning Engine for Long-Term Natural Resource Management Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.20
BuildRequires:    R-CRAN-caret >= 6.0.93
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-pls >= 2.8.0
BuildRequires:    R-CRAN-plm >= 2.6.0
BuildRequires:    R-CRAN-Kendall >= 2.2
BuildRequires:    R-CRAN-strucchange >= 1.5.3
BuildRequires:    R-CRAN-boot >= 1.3.28
BuildRequires:    R-CRAN-trend >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-lavaan >= 0.6.12
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-forecast >= 8.20
Requires:         R-CRAN-caret >= 6.0.93
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-pls >= 2.8.0
Requires:         R-CRAN-plm >= 2.6.0
Requires:         R-CRAN-Kendall >= 2.2
Requires:         R-CRAN-strucchange >= 1.5.3
Requires:         R-CRAN-boot >= 1.3.28
Requires:         R-CRAN-trend >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-lavaan >= 0.6.12
Requires:         R-stats 
Requires:         R-utils 

%description
A comprehensive toolkit for statistical and machine learning-based
analysis of long-term Natural Resource Management (NRM) datasets.
Integrates formula-driven approaches, statistical inference, and machine
learning (ML) models for advanced analytics. Modules cover trend and
structural analysis (Mann-Kendall test, slope estimation, Chow test,
structural break detection), multivariate system modelling (Partial Least
Squares (PLS), Structural Equation Modelling (SEM)), response curve
optimisation, time-series forecasting (Autoregressive Integrated Moving
Average (ARIMA), hybrid models), panel data and treatment effects
(Difference-in-Differences (DiD), causal machine learning), uncertainty
and sensitivity analysis (bootstrap, Monte Carlo, Bayesian), and automated
model selection and performance comparison. Designed for long-term
datasets covering soil, water, crop, and climate domains. Key references:
Mann and Kendall (1945) <doi:10.2307/1907187>; Sen (1968)
<doi:10.1080/01621459.1968.10480934>; Bai and Perron (2003)
<doi:10.1002/jae.659>; Rosseel (2012) <doi:10.18637/jss.v048.i02>;
Croissant and Millo (2008) <doi:10.18637/jss.v027.i02>.

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
