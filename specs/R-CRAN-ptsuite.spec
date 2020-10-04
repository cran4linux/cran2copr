%global packname  ptsuite
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Tail Index Estimation for Power Law Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Various estimation methods for the shape parameter of Pareto distributed
data. This package contains functions for various estimation methods such
as maximum likelihood (Newman, 2005)<doi:10.1016/j.cities.2012.03.001>,
Hill's estimator (Hill, 1975)<doi:10.1214/aos/1176343247>, least squares
(Zaher et al., 2014)<doi:10.9734/BJMCS/2014/10890>, method of moments
(Rytgaard, 1990)<doi:10.2143/AST.20.2.2005443>, percentiles (Bhatti et
al., 2018)<doi:10.1371/journal.pone.0196456>, and weighted least squares
(Nair et al., 2019) to estimate the shape parameter of Pareto distributed
data. It also provides both a heuristic method (Hubert et al.,
2013)<doi:10.1016/j.csda.2012.07.011> and a goodness of fit test (Gulati
and Shapiro, 2008)<doi:10.1007/978-0-8176-4619-6> for testing for Pareto
data as well as a method for generating Pareto distributed data.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
