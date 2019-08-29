%global packname  bgsmtr
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          Bayesian Group Sparse Multi-Task Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.3.3
BuildRequires:    R-CRAN-LaplacesDemon >= 16.1.0
BuildRequires:    R-CRAN-mnormt >= 1.5.4
BuildRequires:    R-CRAN-statmod >= 1.4.26
BuildRequires:    R-Matrix >= 1.2.6
BuildRequires:    R-CRAN-EDISON >= 1.1.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.5
BuildRequires:    R-CRAN-matrixcalc >= 1.0.3
BuildRequires:    R-CRAN-CholWishart >= 0.9.3
BuildRequires:    R-CRAN-miscTools >= 0.6.22
BuildRequires:    R-CRAN-inline >= 0.3.15
BuildRequires:    R-CRAN-sparseMVN >= 0.2.0
BuildRequires:    R-CRAN-coda >= 0.18.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
Requires:         R-methods >= 3.3.3
Requires:         R-CRAN-LaplacesDemon >= 16.1.0
Requires:         R-CRAN-mnormt >= 1.5.4
Requires:         R-CRAN-statmod >= 1.4.26
Requires:         R-Matrix >= 1.2.6
Requires:         R-CRAN-EDISON >= 1.1.1
Requires:         R-CRAN-mvtnorm >= 1.0.5
Requires:         R-CRAN-matrixcalc >= 1.0.3
Requires:         R-CRAN-CholWishart >= 0.9.3
Requires:         R-CRAN-miscTools >= 0.6.22
Requires:         R-CRAN-inline >= 0.3.15
Requires:         R-CRAN-sparseMVN >= 0.2.0
Requires:         R-CRAN-coda >= 0.18.1
Requires:         R-CRAN-Rcpp >= 0.12.14

%description
Fits a Bayesian group-sparse multi-task regression model using Gibbs
sampling. The hierarchical prior encourages shrinkage of the estimated
regression coefficients at both the gene and SNP level. The model has been
extended to a spatial model that allows for two type correlation in
neuroimaging genetics data and been applied successfully to imaging
phenotypes of dimension up to 100; it can be used more generally for
multivariate (non-imaging) phenotypes.

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
