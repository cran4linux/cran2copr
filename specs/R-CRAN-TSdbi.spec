%global packname  TSdbi
%global packver   2017.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2017.4.1
Release:          1%{?dist}
Summary:          Time Series Database Interface

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tframe >= 2015.1.1
BuildRequires:    R-CRAN-DBI >= 0.3.1
BuildRequires:    R-methods 
Requires:         R-CRAN-tframe >= 2015.1.1
Requires:         R-CRAN-DBI >= 0.3.1
Requires:         R-methods 

%description
Provides a common interface to time series databases. The objective is to
define a standard interface so users can retrieve time series data from
various sources with a simple, common, set of commands, and so programs
can be written to be portable with respect to the data source. The SQL
implementations also provide a database table design, so users needing to
set up a time series database have a reasonably complete way to do this
easily. The interface provides for a variety of options with respect to
the representation of time series in R. The interface, and the SQL
implementations, also handle vintages of time series data (sometime called
editions or real-time data). There is also a (not yet well tested)
mechanism to handle multilingual data documentation. Comprehensive
examples of all the 'TS*' packages is provided in the vignette Guide.pdf
with the 'TSdata' package.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
