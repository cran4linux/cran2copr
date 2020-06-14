%global packname  goldi
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Gene Ontology Label Discernment and Identification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-futile.logger 

%description
A tool for identifying multiple word key terms in free text with
application to Gene Ontology labels.

%prep
%setup -q -c -n %{packname}
find %{packname}/inst -type f -exec sed -Ei 's@#!/usr/bin/(env )*python@#!/usr/bin/python2@g' {} \;

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/pdf2txt.py
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
