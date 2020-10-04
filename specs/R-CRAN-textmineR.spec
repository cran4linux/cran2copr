%global packname  textmineR
%global packver   3.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Text Mining and Topic Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-text2vec >= 0.5
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-stopwords 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-text2vec >= 0.5
Requires:         R-Matrix 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-stopwords 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-RSpectra 

%description
An aid for text mining in R, with a syntax that should be familiar to
experienced R users. Provides a wrapper for several topic models that take
similarly-formatted input and give similarly-formatted output. Has
additional functionality for analyzing and diagnostics for topic models.

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
