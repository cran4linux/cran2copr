%global packname  BNPMIXcluster
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          2%{?dist}
Summary:          Bayesian Nonparametric Model for Clustering with Mixed ScaleVariables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-gplots 
Requires:         R-MASS 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-truncnorm 

%description
Bayesian nonparametric approach for clustering that is capable to combine
different types of variables (continuous, ordinal and nominal) and also
accommodates for different sampling probabilities in a complex survey
design. The model is based on a location mixture model with a
Poisson-Dirichlet process prior on the location parameters of the
associated latent variables. The package performs the clustering model
described in Carmona, C., Nieto-Barajas, L. E., Canale, A. (2016)
<arXiv:1612.00083>.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
