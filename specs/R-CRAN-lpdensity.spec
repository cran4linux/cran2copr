%global packname  lpdensity
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Local Polynomial Density Estimation and Inference

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
Without imposing stringent distributional assumptions or shape
restrictions, nonparametric density estimation has been popular in
economics and other social sciences for counterfactual analysis, program
evaluation, and policy recommendations. This package implements a novel
density estimator based on local polynomial regressions, documented in
Cattaneo, Jansson and Ma (2019a, b) <arXiv:1811.11512, arXiv:1906.06529>:
lpdensity() to construct local polynomial based density (and derivatives)
estimator; lpbwdensity() to perform data-driven bandwidth selection; and
lpdensity.plot() for density plot with robust confidence interval.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
