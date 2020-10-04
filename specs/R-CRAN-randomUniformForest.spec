%global packname  randomUniformForest
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Random Uniform Forests for Classification, Regression andUnsupervised Learning

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-foreach >= 1.4.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-cluster 
BuildRequires:    R-MASS 
Requires:         R-CRAN-foreach >= 1.4.2
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-gtools 
Requires:         R-cluster 
Requires:         R-MASS 

%description
Ensemble model, for classification, regression and unsupervised learning,
based on a forest of unpruned and randomized binary decision trees. Each
tree is grown by sampling, with replacement, a set of variables at each
node. Each cut-point is generated randomly, according to the continuous
Uniform distribution. For each tree, data are either bootstrapped or
subsampled. The unsupervised mode introduces clustering, dimension
reduction and variable importance, using a three-layer engine. Random
Uniform Forests are mainly aimed to lower correlation between trees (or
trees residuals), to provide a deep analysis of variable importance and to
allow native distributed and incremental learning.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
