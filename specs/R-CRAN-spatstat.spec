%global packname  spatstat
%global packver   1.63-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.63.3
Release:          1%{?dist}
Summary:          Spatial Point Pattern Analysis, Model-Fitting, Simulation, Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-spatstat.data >= 1.4.2
BuildRequires:    R-CRAN-goftest >= 1.2.2
BuildRequires:    R-CRAN-spatstat.utils >= 1.17.0
BuildRequires:    R-CRAN-polyclip >= 1.10.0
BuildRequires:    R-CRAN-deldir >= 0.0.21
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-nlme 
BuildRequires:    R-rpart 
BuildRequires:    R-mgcv 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-tensor 
Requires:         R-CRAN-spatstat.data >= 1.4.2
Requires:         R-CRAN-goftest >= 1.2.2
Requires:         R-CRAN-spatstat.utils >= 1.17.0
Requires:         R-CRAN-polyclip >= 1.10.0
Requires:         R-CRAN-deldir >= 0.0.21
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-nlme 
Requires:         R-rpart 
Requires:         R-mgcv 
Requires:         R-Matrix 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-tensor 

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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ratfor
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
