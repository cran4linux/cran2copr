%global packname  MARSS
%global packver   3.10.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.10.12
Release:          2%{?dist}
Summary:          Multivariate Autoregressive State-Space Modeling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-KFAS >= 1.0.1
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-KFAS >= 1.0.1
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-mvtnorm 
Requires:         R-nlme 
Requires:         R-stats 
Requires:         R-utils 

%description
The MARSS package provides maximum-likelihood parameter estimation for
constrained and unconstrained linear multivariate autoregressive
state-space (MARSS) models fit to multivariate time-series data.  Fitting
is primarily via an Expectation-Maximization (EM) algorithm, although
fitting via the BFGS algorithm (using the optim function) is also
provided.  MARSS models are a class of dynamic linear model (DLM) and
vector autoregressive model (VAR) model.  Functions are provided for
parametric and innovations bootstrapping, Kalman filtering and smoothing,
bootstrap model selection criteria (AICb), confidences intervals via the
Hessian approximation and via bootstrapping and calculation of auxiliary
residuals for detecting outliers and shocks.  The user guide shows
examples of using MARSS for parameter estimation for a variety of
applications, model selection, dynamic factor analysis, outlier and shock
detection, and addition of covariates.  Type RShowDoc("UserGuide",
package="MARSS") at the R command line to open the MARSS user guide.
Online workshops (lectures and computer labs) at
<https://nwfsc-timeseries.github.io/> See the NEWS file for update
information.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
