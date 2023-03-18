%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Multiaovbay
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Classic, Nonparametric and Bayesian Two-Way Analysis of Variance Panel

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinydashboardPlus 
BuildRequires:    R-CRAN-ggstatsplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-highcharter 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-PMCMRplus 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-waiter 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-ggstatsplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-car 
Requires:         R-CRAN-highcharter 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-PMCMRplus 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-waiter 
Requires:         R-CRAN-htmltools 
Requires:         R-graphics 
Requires:         R-stats 

%description
Covers several approaches to ANOVA (Analysis of Variance), specifically
studying a balanced two-factor fixed-fixed ANOVA design. It consists of
four sections. The first section uses a dynamic scheme to indicate which
possible alternatives to follow depending on the fulfillment of the
assumptions of the model. It also presents an analysis on the fulfillment
of the assumptions of linearity, homoscedasticity, normality, and
independence in the residuals of the model, as well as dynamic statistical
graphs on the residuals of the model. The second section presents an
analysis with a non-parametric approach of Kruskal Wallis. After Kruskal
Wallis, a Post-Hoc analysis of multiple comparisons on the medians of the
treatments is carried out. The third section presents a classical
parametric ANOVA. Following classical ANOVA, a post-hoc analysis of
multiple comparisons on the medians of the treatments, factor levels by
Dunn's test, and statistical graphs for the treatments and factor levels
are shown. Additionally, a post-hoc analysis of multiple comparisons on
the means of the treatments is done. The fourth section presents an
analysis of variance under a Bayesian approach. In this section,
interactive statistical graphs are presented on the posterior
distributions of treatments, factor levels, and a convergence analysis of
the estimated parameters, using MCMC (Markov Chain Monte Carlo). These
results are displayed in an interactive glossy panel which allows
modification of the test arguments, contains interactive statistical
plots, and presents automatic conclusions depending on the fulfillment of
the assumptions of the balanced two-factor fixed ANOVA model.

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
