%global packname  nc
%global packver   2020.3.23
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2020.3.23
Release:          1%{?dist}
Summary:          Named Capture to Data Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-data.table 

%description
User-friendly functions for extracting a data table (row for each match,
column for each group) from non-tabular text data using regular
expressions, and for melting columns that match a regular expression.
Patterns are defined using a readable syntax that makes it easy to build
complex patterns in terms of simpler, re-usable sub-patterns. Named R
arguments are translated to column names in the output; capture groups
without names are used internally in order to provide a standard interface
to three regular expression C libraries (PCRE, RE2, ICU). Output can also
include numeric columns via user-specified type conversion functions. RE2
engine (re2r package) was removed from CRAN in Mar 2020 so must be
installed from github.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/test_engines.R
%{rlibdir}/%{packname}/INDEX
