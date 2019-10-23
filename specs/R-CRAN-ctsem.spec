%global packname  ctsem
%global packver   3.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.4
Release:          1%{?dist}
Summary:          Continuous Time Structural Equation Modelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-OpenMx >= 2.9.0
BuildRequires:    R-CRAN-rstan >= 2.19.0
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0.1
BuildRequires:    R-CRAN-rstantools >= 1.5.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-Matrix 
BuildRequires:    R-datasets 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mize 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-CRAN-cOde 
BuildRequires:    R-CRAN-Deriv 
Requires:         R-CRAN-OpenMx >= 2.9.0
Requires:         R-CRAN-rstan >= 2.19.0
Requires:         R-CRAN-rstantools >= 1.5.0
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-plyr 
Requires:         R-tools 
Requires:         R-CRAN-data.table 
Requires:         R-Matrix 
Requires:         R-datasets 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mize 
Requires:         R-CRAN-pkgbuild 
Requires:         R-CRAN-cOde 
Requires:         R-CRAN-Deriv 

%description
Hierarchical continuous time state space modelling, for linear and
nonlinear systems measured by continuous variables, with limited support
for binary data. The subject specific dynamic system is modelled as a
stochastic differential equation (SDE), measurement models are typically
multivariate normal factor models. Using the original ctsem formulation
based on OpenMx, described in the JSS paper "Continuous Time Structural
Equation Modeling with R Package ctsem", with updated version as CRAN
vignette
<https://cran.r-project.org/web/packages/ctsem/vignettes/ctsem.pdf> ,
linear mixed effects SDE's estimated via maximum likelihood and
optimization are possible. Using the Stan based formulation, described in
<https://github.com/cdriveraus/ctsem/raw/master/vignettes/hierarchicalmanual.pdf>
, nonlinearity (state dependent parameters) and random effects on all
parameters are possible, using either optimization (with optional
importance sampling) or Stan's Hamiltonian Monte Carlo sampling. Priors
may be used. For the conceptual overview of the hierarchical Bayesian
linear SDE approach, see
<https://www.researchgate.net/publication/324093594_Hierarchical_Bayesian_Continuous_Time_Dynamic_Modeling>.
Exogenous inputs may also be included, for an overview of such
possibilities see
<https://www.researchgate.net/publication/328221807_Understanding_the_Time_Course_of_Interventions_with_Continuous_Time_Dynamic_Models>
. Stan based functions are not available on 32 bit Windows systems at
present.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
