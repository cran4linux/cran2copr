%global packname  xslt
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Extensible Style-Sheet Language Transformations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libxslt-devel
Requires:         libxslt
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-xml2 >= 1.1.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-xml2 >= 1.1.0

%description
An extension for the 'xml2' package to transform XML documents by applying
an 'xslt' style-sheet.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
