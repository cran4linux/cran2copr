%global __brp_check_rpaths %{nil}
%global packname  revgeo
%global packver   0.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15
Release:          3%{?dist}%{?buildtag}
Summary:          Reverse Geocoding with the Photon Geocoder for OpenStreetMap,Google Maps, and Bing

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl >= 1.95
BuildRequires:    R-CRAN-RJSONIO >= 1.3.0
Requires:         R-CRAN-RCurl >= 1.95
Requires:         R-CRAN-RJSONIO >= 1.3.0

%description
Function revgeo() allows you to use the Photon geocoder for OpenStreetMap
<http://photon.komoot.de>, Google Maps <http://maps.google.com>, and Bing
<https://www.bingmapsportal.com> to reverse geocode coordinate pairs with
minimal hassle.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
