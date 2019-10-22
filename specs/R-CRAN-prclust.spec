%global packname  prclust
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Penalized Regression-Based Clustering Method

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-parallel 
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-parallel 

%description
Clustering is unsupervised and exploratory in nature. Yet, it can be
performed through penalized regression with grouping pursuit. In this
package, we provide two algorithms for fitting the penalized
regression-based clustering (PRclust) with non-convex grouping penalties,
such as group truncated lasso, MCP and SCAD. One algorithm is based on
quadratic penalty and difference convex method. Another algorithm is based
on difference convex and ADMM, called DC-ADD, which is more efficient.
Generalized cross validation and stability based method were provided to
select the tuning parameters. Rand index, adjusted Rand index and Jaccard
index were provided to estimate the agreement between estimated cluster
memberships and the truth.

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
%{rlibdir}/%{packname}/libs
