%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatstat.linnet
%global packver   3.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Networks Functionality of the 'spatstat' Family

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-spatstat.model >= 3.2.1
BuildRequires:    R-CRAN-spatstat.random >= 3.1.3
BuildRequires:    R-CRAN-spatstat.geom >= 3.0.6
BuildRequires:    R-CRAN-spatstat.explore >= 3.0.6
BuildRequires:    R-CRAN-spatstat.data >= 3.0
BuildRequires:    R-CRAN-spatstat.utils >= 3.0
BuildRequires:    R-CRAN-spatstat.sparse >= 3.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-spatstat.model >= 3.2.1
Requires:         R-CRAN-spatstat.random >= 3.1.3
Requires:         R-CRAN-spatstat.geom >= 3.0.6
Requires:         R-CRAN-spatstat.explore >= 3.0.6
Requires:         R-CRAN-spatstat.data >= 3.0
Requires:         R-CRAN-spatstat.utils >= 3.0
Requires:         R-CRAN-spatstat.sparse >= 3.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 

%description
Defines types of spatial data on a linear network and provides
functionality for geometrical operations, data analysis and modelling of
data on a linear network, in the 'spatstat' family of packages. Contains
definitions and support for linear networks, including creation of
networks, geometrical measurements, topological connectivity, geometrical
operations such as inserting and deleting vertices, intersecting a network
with another object, and interactive editing of networks. Data types
defined on a network include point patterns, pixel images, functions, and
tessellations. Exploratory methods include kernel estimation of intensity
on a network, K-functions and pair correlation functions on a network,
simulation envelopes, nearest neighbour distance and empty space distance,
relative risk estimation with cross-validated bandwidth selection. Formal
hypothesis tests of random pattern (chi-squared, Kolmogorov-Smirnov, Monte
Carlo, Diggle-Cressie-Loosmore-Ford, Dao-Genton, two-stage Monte Carlo)
and tests for covariate effects (Cox-Berman-Waller-Lawson,
Kolmogorov-Smirnov, ANOVA) are also supported. Parametric models can be
fitted to point pattern data using the function lppm() similar to glm().
Only Poisson models are implemented so far. Models may involve dependence
on covariates and dependence on marks. Models are fitted by maximum
likelihood. Fitted point process models can be simulated, automatically.
Formal hypothesis tests of a fitted model are supported (likelihood ratio
test, analysis of deviance, Monte Carlo tests) along with basic tools for
model selection (stepwise(), AIC()) and variable selection (sdr). Tools
for validating the fitted model include simulation envelopes, residuals,
residual plots and Q-Q plots, leverage and influence diagnostics, partial
residuals, and added variable plots. Random point patterns on a network
can be generated using a variety of models.

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
