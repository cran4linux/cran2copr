%global packname  quanteda.textmodels
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Scaling Models and Classifiers for Textual Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-quanteda >= 2.0
BuildRequires:    R-Matrix >= 1.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.600.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-LiblineaR 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RSSL 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-quanteda >= 2.0
Requires:         R-Matrix >= 1.2
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-LiblineaR 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-RSSL 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-stringi 

%description
Scaling models and classifiers for sparse matrix objects representing
textual data in the form of a document-feature matrix.  Includes original
implementations of 'Laver', 'Benoit', and Garry's (2003)
<doi:10.1017/S0003055403000698>, 'Wordscores' model, Perry and 'Benoit's'
(2017) <arXiv:1710.08963> class affinity scaling model, and 'Slapin' and
'Proksch's' (2008) <doi:10.1111/j.1540-5907.2008.00338.x> 'wordfish'
model, as well as methods for correspondence analysis, latent semantic
analysis, and fast Naive Bayes and linear 'SVMs' specially designed for
sparse textual data.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
