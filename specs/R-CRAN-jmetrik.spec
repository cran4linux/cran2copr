%global packname  jmetrik
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Interacting with 'jMetrik'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The main purpose of this package is to make it easy for userR's to
interact with 'jMetrik' an open source application for psychometric
analysis. For example it allows useR's to write data frames to file in a
format that can be used by 'jMetrik'. It also allows useR's to read
*.jmetrik files (e.g. output from an analysis) for follow-up analysis in
R. The *.jmetrik format is a flat file that includes a multiline header
and the data as comma separated values. The header includes metadata about
the file and one row per variable with the following information in each
row: variable name, data type, item scoring, special data codes, and
variable label.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
