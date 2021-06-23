%global __brp_check_rpaths %{nil}
%global packname  timeDate
%global packver   3043.102
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3043.102
Release:          3%{?dist}%{?buildtag}
Summary:          Rmetrics - Chronological and Calendar Objects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 

%description
The 'timeDate' class fulfils the conventions of the ISO 8601 standard as
well as of the ANSI C and POSIX standards. Beyond these standards it
provides the "Financial Center" concept which allows to handle data
records collected in different time zones and mix them up to have always
the proper time stamps with respect to your personal financial center, or
alternatively to the GMT reference time. It can thus also handle time
stamps from historical data records from the same time zone, even if the
financial centers changed day light saving times at different calendar
dates.

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
%doc %{rlibdir}/%{packname}/COPYRIGHT.html
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
