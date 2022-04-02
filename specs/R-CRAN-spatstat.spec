%global __brp_check_rpaths %{nil}
%global packname  spatstat
%global packver   2.3-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Point Pattern Analysis, Model-Fitting, Simulation, Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat.core >= 2.4.1
BuildRequires:    R-CRAN-spatstat.geom >= 2.4.0
BuildRequires:    R-CRAN-spatstat.linnet >= 2.3.2
BuildRequires:    R-CRAN-spatstat.utils >= 2.3.0
BuildRequires:    R-CRAN-spatstat.random >= 2.2.0
BuildRequires:    R-CRAN-spatstat.data >= 2.1.2
BuildRequires:    R-utils 
Requires:         R-CRAN-spatstat.core >= 2.4.1
Requires:         R-CRAN-spatstat.geom >= 2.4.0
Requires:         R-CRAN-spatstat.linnet >= 2.3.2
Requires:         R-CRAN-spatstat.utils >= 2.3.0
Requires:         R-CRAN-spatstat.random >= 2.2.0
Requires:         R-CRAN-spatstat.data >= 2.1.2
Requires:         R-utils 

%description
Comprehensive open-source toolbox for analysing Spatial Point Patterns.
Focused mainly on two-dimensional point patterns, including
multitype/marked points, in any spatial region. Also supports
three-dimensional point patterns, space-time point patterns in any number
of dimensions, point patterns on a linear network, and patterns of other
geometrical objects. Supports spatial covariate data such as pixel images.
Contains over 2000 functions for plotting spatial data, exploratory data
analysis, model-fitting, simulation, spatial sampling, model diagnostics,
and formal inference. Data types include point patterns, line segment
patterns, spatial windows, pixel images, tessellations, and linear
networks. Exploratory methods include quadrat counts, K-functions and
their simulation envelopes, nearest neighbour distance and empty space
statistics, Fry plots, pair correlation function, kernel smoothed
intensity, relative risk estimation with cross-validated bandwidth
selection, mark correlation functions, segregation indices, mark
dependence diagnostics, and kernel estimates of covariate effects. Formal
hypothesis tests of random pattern (chi-squared, Kolmogorov-Smirnov, Monte
Carlo, Diggle-Cressie-Loosmore-Ford, Dao-Genton, two-stage Monte Carlo)
and tests for covariate effects (Cox-Berman-Waller-Lawson,
Kolmogorov-Smirnov, ANOVA) are also supported. Parametric models can be
fitted to point pattern data using the functions ppm(), kppm(), slrm(),
dppm() similar to glm(). Types of models include Poisson, Gibbs and Cox
point processes, Neyman-Scott cluster processes, and determinantal point
processes. Models may involve dependence on covariates, inter-point
interaction, cluster formation and dependence on marks. Models are fitted
by maximum likelihood, logistic regression, minimum contrast, and
composite likelihood methods. A model can be fitted to a list of point
patterns (replicated point pattern data) using the function mppm(). The
model can include random effects and fixed effects depending on the
experimental design, in addition to all the features listed above. Fitted
point process models can be simulated, automatically. Formal hypothesis
tests of a fitted model are supported (likelihood ratio test, analysis of
deviance, Monte Carlo tests) along with basic tools for model selection
(stepwise(), AIC()) and variable selection (sdr). Tools for validating the
fitted model include simulation envelopes, residuals, residual plots and
Q-Q plots, leverage and influence diagnostics, partial residuals, and
added variable plots.

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
