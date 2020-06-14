%global packname  jeek
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          A Fast and Scalable Joint Estimator for Integrating AdditionalKnowledge in Learning Multiple Related Sparse GaussianGraphical Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-igraph 

%description
Provides a fast and scalable joint estimator for integrating additional
knowledge in learning multiple related sparse Gaussian Graphical Models
(JEEK). The JEEK algorithm can be used to fast estimate multiple related
precision matrices in a large-scale. For instance, it can identify
multiple gene networks from multi-context gene expression datasets. By
performing data-driven network inference from high-dimensional and
heterogeneous data sets, this tool can help users effectively translate
aggregated data into knowledge that take the form of graphs among
entities. Please run demo(jeek) to learn the basic functions provided by
this package. For further details, please read the original paper: Beilun
Wang, Arshdeep Sekhon, Yanjun Qi "A Fast and Scalable Joint Estimator for
Integrating Additional Knowledge in Learning Multiple Related Sparse
Gaussian Graphical Models" (ICML 2018) <arXiv:1806.00548>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
