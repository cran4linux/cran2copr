%global packname  huge
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          High-Dimensional Undirected Graph Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-MASS 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
Provides a general framework for high-dimensional undirected graph
estimation. It integrates data preprocessing, neighborhood screening,
graph estimation, and model selection techniques into a pipeline. In
preprocessing stage, the nonparanormal(npn) transformation is applied to
help relax the normality assumption. In the graph estimation stage, the
graph structure is estimated by Meinshausen-Buhlmann graph estimation or
the graphical lasso, and both methods can be further accelerated by the
lossy screening rule preselecting the neighborhood of each variable by
correlation thresholding. We target on high-dimensional data analysis
usually d >> n, and the computation is memory-optimized using the sparse
matrix output. We also provide a computationally efficient approach,
correlation thresholding graph estimation. Three
regularization/thresholding parameter selection methods are included in
this package: (1)stability approach for regularization selection (2)
rotation information criterion (3) extended Bayesian information criterion
which is only available for the graphical lasso.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
