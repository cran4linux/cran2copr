%global packname  ical
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}
Summary:          'iCalendar' Parsing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-V8 >= 1.5
Requires:         R-CRAN-V8 >= 1.5

%description
A simple wrapper around the 'ical.js' library executing 'Javascript' code
via 'V8' (the 'Javascript' engine driving the 'Chrome' browser and
'Node.js' and accessible via the 'V8' R package). This package enables
users to parse 'iCalendar' files ('.ics', '.ifb', '.iCal', '.iFBf') into
lists and 'data.frames' to ultimately do statistics on events, meetings,
schedules, birthdays, and the like.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/birthdays.ics
%doc %{rlibdir}/%{packname}/ical.js
%{rlibdir}/%{packname}/INDEX
