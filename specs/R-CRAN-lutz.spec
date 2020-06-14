%global packname  lutz
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          Look Up Time Zones of Point Coordinates

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-lubridate 

%description
Input latitude and longitude values or an 'sf/sfc' POINT object and get
back the time zone in which they exist. Two methods are implemented. One
is very fast and uses 'Rcpp' in conjunction with data from the
'Javascript' library (<https://github.com/darkskyapp/tz-lookup/>). This
method also works outside of countries' borders and in international
waters, however speed comes at the cost of accuracy - near time zone
borders away from populated centres there is a chance that it will return
the incorrect time zone. The other method is slower but more accurate - it
uses the 'sf' package to intersect points with a detailed map of time
zones from here:
<https://github.com/evansiroky/timezone-boundary-builder/>. The package
also contains several utility functions for helping to understand and
visualize time zones, such as listing of world time zones, including
information about daylight savings times and their offsets from UTC. You
can also plot a time zone to visualize the UTC offset over a year and when
daylight savings times are in effect.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
