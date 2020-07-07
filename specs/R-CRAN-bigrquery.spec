%global packname  bigrquery
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}
Summary:          An Interface to Google's 'BigQuery' 'API'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-gargle >= 0.5.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rapidjsonr 
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-gargle >= 0.5.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Easily talk to Google's 'BigQuery' database from R.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/secret
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
