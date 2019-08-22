%global packname  tgp
%global packver   2.4-14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.14
Release:          1%{?dist}
Summary:          Bayesian Treed Gaussian Process Models

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-maptree 
Requires:         R-CRAN-maptree 

%description
Bayesian nonstationary, semiparametric nonlinear regression and design by
treed Gaussian processes (GPs) with jumps to the limiting linear model
(LLM).  Special cases also implemented include Bayesian linear models,
CART, treed linear models, stationary separable and isotropic GPs, and GP
single-index models.  Provides 1-d and 2-d plotting functions (with
projection and slice capabilities) and tree drawing, designed for
visualization of tgp-class output.  Sensitivity analysis and
multi-resolution models are supported. Sequential experimental design and
adaptive sampling functions are also provided, including ALM, ALC, and
expected improvement.  The latter supports derivative-free optimization of
noisy black-box functions.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
