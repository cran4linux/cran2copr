%global packname  BAMMtools
%global packver   2.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.6
Release:          1%{?dist}
Summary:          Analysis and Visualization of Macroevolutionary Dynamics onPhylogenetic Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-ape 
Requires:         R-CRAN-gplots 
Requires:         R-methods 

%description
Provides functions for analyzing and visualizing complex macroevolutionary
dynamics on phylogenetic trees. It is a companion package to the command
line program BAMM (Bayesian Analysis of Macroevolutionary Mixtures) and is
entirely oriented towards the analysis, interpretation, and visualization
of evolutionary rates. Functionality includes visualization of rate shifts
on phylogenies, estimating evolutionary rates through time, comparing
posterior distributions of evolutionary rates across clades, comparing
diversification models using Bayes factors, and more.

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
%{rlibdir}/%{packname}/libs
