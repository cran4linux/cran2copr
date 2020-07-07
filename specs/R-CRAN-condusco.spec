%global packname  condusco
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Query-Driven Pipeline Execution and Query Templates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-bigrquery 
BuildRequires:    R-CRAN-DBI 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-bigrquery 
Requires:         R-CRAN-DBI 

%description
Runs a function iteratively over each row of either a dataframe or the
results of a query.  Use the 'BigQuery' and 'DBI' wrappers to iteratively
pass each row of query results to a function.  If a field contains a
'JSON' string, it will be converted to an object.  This is helpful for
queries that return 'JSON' strings that represent objects. These fields
can then be treated as objects by the pipeline.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
