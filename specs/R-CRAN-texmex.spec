%global packname  texmex
%global packver   2.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.7
Release:          1%{?dist}
Summary:          Statistical Modelling of Extreme Values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
Statistical extreme value modelling of threshold excesses, maxima and
multivariate extremes. Univariate models for threshold excesses and maxima
are the Generalised Pareto, and Generalised Extreme Value model
respectively. These models may be fitted by using maximum (optionally
penalised-)likelihood, or Bayesian estimation, and both classes of models
may be fitted with covariates in any/all model parameters. Model
diagnostics support the fitting process. Graphical output for visualising
fitted models and return level estimates is provided. For serially
dependent sequences, the intervals declustering algorithm of Ferro and
Segers (2003) <doi:10.1111/1467-9868.00401> is provided, with diagnostic
support to aid selection of threshold and declustering horizon.
Multivariate modelling is performed via the conditional approach of
Heffernan and Tawn (2004) <doi:10.1111/j.1467-9868.2004.02050.x>, with
graphical tools for threshold selection and to diagnose estimation
convergence.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
