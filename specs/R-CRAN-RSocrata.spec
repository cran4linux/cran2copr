%global packname  RSocrata
%global packver   1.7.10-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.10.6
Release:          3%{?dist}
Summary:          Download or Upload 'Socrata' Data Sets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 0.9
BuildRequires:    R-CRAN-mime >= 0.3
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-jsonlite >= 0.9
Requires:         R-CRAN-mime >= 0.3

%description
Provides easier interaction with 'Socrata' open data portals
<http://dev.socrata.com>. Users can provide a 'Socrata' data set resource
URL, or a 'Socrata' Open Data API (SoDA) web query, or a 'Socrata'
"human-friendly" URL, returns an R data frame. Converts dates to 'POSIX'
format and manages throttling by 'Socrata'. Users can upload data to
'Socrata' portals directly from R.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
