%global packname  sqldf
%global packver   0.4-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.11
Release:          2%{?dist}
Summary:          Manipulate R Data Frames Using SQL

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gsubfn >= 0.6
BuildRequires:    R-CRAN-proto 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-chron 
Requires:         R-CRAN-gsubfn >= 0.6
Requires:         R-CRAN-proto 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-chron 

%description
The sqldf() function is typically passed a single argument which is an SQL
select statement where the table names are ordinary R data frame names.
sqldf() transparently sets up a database, imports the data frames into
that database, performs the SQL select or other statement and returns the
result using a heuristic to determine which class to assign to each column
of the returned data frame.  The sqldf() or read.csv.sql() functions can
also be used to read filtered files into R even if the original files are
larger than R itself can handle. 'RSQLite', 'RH2', 'RMySQL' and
'RPostgreSQL' backends are supported.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/csv.awk
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/THANKS
%doc %{rlibdir}/%{packname}/trcomma2dot.vbs
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
