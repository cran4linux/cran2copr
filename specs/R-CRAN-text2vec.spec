%global packname  text2vec
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Modern Text Mining Framework for R

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-RcppParallel >= 4.3.14
BuildRequires:    R-CRAN-irlba >= 2.2.1
BuildRequires:    R-CRAN-R6 >= 2.1.2
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-futile.logger >= 1.4.3
BuildRequires:    R-CRAN-stringi >= 1.1.5
BuildRequires:    R-Matrix >= 1.1
BuildRequires:    R-CRAN-digest >= 0.6.8
BuildRequires:    R-CRAN-sparsepp >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.11
BuildRequires:    R-CRAN-mlapi >= 0.1.0
BuildRequires:    R-methods 
Requires:         R-CRAN-RcppParallel >= 4.3.14
Requires:         R-CRAN-irlba >= 2.2.1
Requires:         R-CRAN-R6 >= 2.1.2
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-futile.logger >= 1.4.3
Requires:         R-CRAN-stringi >= 1.1.5
Requires:         R-Matrix >= 1.1
Requires:         R-CRAN-digest >= 0.6.8
Requires:         R-CRAN-Rcpp >= 0.11
Requires:         R-CRAN-mlapi >= 0.1.0
Requires:         R-methods 

%description
Fast and memory-friendly tools for text vectorization, topic modeling
(LDA, LSA), word embeddings (GloVe), similarities. This package provides a
source-agnostic streaming API, which allows researchers to perform
analysis of collections of documents which are larger than available RAM.
All core functions are parallelized to benefit from multicore machines.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
