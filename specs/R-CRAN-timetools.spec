%global packname  timetools
%global packver   1.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.14
Release:          1%{?dist}
Summary:          Seasonal/Sequential (Instants/Durations, Even or not) TimeSeries

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Objects to manipulate sequential and seasonal time series. Sequential time
series based on time instants and time durations are handled. Both can be
regularly or unevenly spaced (overlapping durations are allowed). Only
POSIX* format are used for dates and times. The following classes are
provided : 'POSIXcti', 'POSIXctp', 'TimeIntervalDataFrame',
'TimeInstantDataFrame', 'SubtimeDataFrame' ; methods to switch from a
class to another and to modify the time support of series (hourly time
series to daily time series for instance) are also defined. Tools provided
can be used for instance to handle environmental monitoring data (not
always produced on a regular time base).

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
