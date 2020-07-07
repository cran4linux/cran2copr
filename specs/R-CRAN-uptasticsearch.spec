%global packname  uptasticsearch
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}
Summary:          Get Data Frame Representations of 'Elasticsearch' Results

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-uuid 

%description
'Elasticsearch' is an open-source, distributed, document-based datastore
(<https://www.elastic.co/products/elasticsearch>). It provides an 'HTTP'
'API' for querying the database and extracting datasets, but that 'API'
was not designed for common data science workflows like pulling large
batches of records and normalizing those documents into a data frame that
can be used as a training dataset for statistical models. 'uptasticsearch'
provides an interface for 'Elasticsearch' that is explicitly designed to
make these data science workflows easy and fun.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
