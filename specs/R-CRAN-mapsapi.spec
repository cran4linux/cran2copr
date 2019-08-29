%global packname  mapsapi
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          'sf'-Compatible Interface to 'Google Maps' APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-xml2 >= 1.1.1
BuildRequires:    R-CRAN-bitops >= 1.0.6
BuildRequires:    R-CRAN-sf >= 0.5.3
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-xml2 >= 1.1.1
Requires:         R-CRAN-bitops >= 1.0.6
Requires:         R-CRAN-sf >= 0.5.3

%description
Interface to the 'Google Maps' APIs: (1) routing directions based on the
'Directions' API, returned as 'sf' objects, either as single feature per
alternative route, or a single feature per segment per alternative route;
(2) travel distance or time matrices based on the 'Distance Matrix' API;
(3) geocoded locations based on the 'Geocode' API, returned as 'sf'
objects, either points or bounds.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
