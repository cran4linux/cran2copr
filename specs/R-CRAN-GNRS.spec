%global packname  GNRS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Access the 'Geographic Name Resolution Service'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-jsonlite 

%description
Provides tools for interacting with the 'geographic name resolution
service' ('GNRS') API <https://github.com/ojalaquellueva/gnrs> and
associated functionality. The 'GNRS' is a batch application for resolving
& standardizing political division names against standard name in the
geonames database <http://www.geonames.org/>. The 'GNRS' resolves
political division names at three levels: country, state/province and
county/parish. Resolution is performed in a series of steps, beginning
with direct matching to standard names, followed by direct matching to
alternate names in different languages, followed by direct matching to
standard codes (such as ISO and FIPS codes). If direct matching fails, the
'GNRS' attempts to match to standard and then alternate names using fuzzy
matching, but does not perform fuzzing matching of political division
codes. The 'GNRS' works down the political division hierarchy, stopping at
the current level if all matches fail. In other words, if a country cannot
be matched, the 'GNRS' does not attempt to match state or county.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
