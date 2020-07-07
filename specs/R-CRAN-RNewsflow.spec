%global packname  RNewsflow
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          3%{?dist}
Summary:          Tools for Comparing Text Messages Across Time and Media

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-Matrix >= 1.2
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-Matrix >= 1.2
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-wordcloud 
Requires:         R-methods 
Requires:         R-CRAN-quanteda 

%description
A collection of tools for measuring the similarity of text messages and
tracing the flow of messages over time and across media.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
