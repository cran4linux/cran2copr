%global packname  phyr
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Model Based Phylogenetic Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-Rcpp 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-latticeExtra 

%description
A collection of functions to do model-based phylogenetic analysis. It
includes functions to calculate community phylogenetic diversity, to
estimate correlations among functional traits while accounting for
phylogenetic relationships, and to fit phylogenetic generalized linear
mixed models. The Bayesian phylogenetic generalized linear mixed models
are fitted with the 'INLA' package (<http://www.r-inla.org>).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extra_data
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
