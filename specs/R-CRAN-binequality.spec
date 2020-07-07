%global packname  binequality
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}
Summary:          Methods for Analyzing Binned Income Data

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss.dist >= 4.3.0
BuildRequires:    R-CRAN-gamlss >= 4.2.7
BuildRequires:    R-CRAN-gamlss.cens >= 4.2.7
BuildRequires:    R-survival >= 2.37.7
BuildRequires:    R-CRAN-ineq >= 0.2.11
Requires:         R-CRAN-gamlss.dist >= 4.3.0
Requires:         R-CRAN-gamlss >= 4.2.7
Requires:         R-CRAN-gamlss.cens >= 4.2.7
Requires:         R-survival >= 2.37.7
Requires:         R-CRAN-ineq >= 0.2.11

%description
Methods for model selection, model averaging, and calculating metrics,
such as the Gini, Theil, Mean Log Deviation, etc, on binned income data
where the topmost bin is right-censored.  We provide both a non-parametric
method, termed the bounded midpoint estimator (BME), which assigns cases
to their bin midpoints; except for the censored bins, where cases are
assigned to an income estimated by fitting a Pareto distribution. Because
the usual Pareto estimate can be inaccurate or undefined, especially in
small samples, we implement a bounded Pareto estimate that yields much
better results.  We also provide a parametric approach, which fits
distributions from the generalized beta (GB) family. Because some GB
distributions can have poor fit or undefined estimates, we fit 10
GB-family distributions and use multimodel inference to obtain definite
estimates from the best-fitting distributions. We also provide binned
income data from all United States of America school districts, counties,
and states.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
