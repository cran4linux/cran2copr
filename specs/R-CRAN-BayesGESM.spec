%global packname  BayesGESM
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          3%{?dist}
Summary:          Bayesian Analysis of Generalized Elliptical Semi-ParametricModels and Flexible Measurement Error Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-normalp 
BuildRequires:    R-CRAN-Formula 
Requires:         R-splines 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-normalp 
Requires:         R-CRAN-Formula 

%description
Set of tools to perform the statistical inference based on the Bayesian
approach for regression models under the assumption that independent
additive errors follow normal, Student-t, slash, contaminated normal,
Laplace or symmetric hyperbolic distributions, i.e., additive errors
follow a scale mixtures of normal distributions. The regression models
considered in this package are: (i) Generalized elliptical semi-parametric
models, where both location and dispersion parameters of the response
variable distribution include non-parametric additive components described
by using B-splines; and (ii) Flexible measurement error models under the
presence of homoscedastic and heteroscedastic random errors, which admit
explanatory variables with and without measurement additive errors as well
as the presence of a non-parametric components approximated by using
B-splines.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
