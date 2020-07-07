%global packname  bnlearn
%global packver   4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5
Release:          3%{?dist}
Summary:          Bayesian Network Structure Learning, Parameter Learning andInference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Bayesian network structure learning, parameter learning and inference.
This package implements constraint-based (PC, GS, IAMB, Inter-IAMB,
Fast-IAMB, MMPC, Hiton-PC, HPC), pairwise (ARACNE and Chow-Liu),
score-based (Hill-Climbing and Tabu Search) and hybrid (MMHC, RSMAX2,
H2PC) structure learning algorithms for discrete, Gaussian and conditional
Gaussian networks, along with many score functions and conditional
independence tests. The Naive Bayes and the Tree-Augmented Naive Bayes
(TAN) classifiers are also implemented. Some utility functions (model
comparison and manipulation, random data generation, arc orientation
testing, simple and advanced plots) are included, as well as support for
parameter estimation (maximum likelihood and Bayesian) and inference,
conditional probability queries, cross-validation, bootstrap and model
averaging. Development snapshots with the latest bugfixes are available
from <http://www.bnlearn.com>.

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
