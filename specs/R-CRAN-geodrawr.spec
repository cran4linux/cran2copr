%global packname  geodrawr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Making Geospatial Objects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.0
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-sf >= 0.9.0
BuildRequires:    R-CRAN-shinydashboard >= 0.7.0
Requires:         R-CRAN-leaflet >= 2.0.0
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-sf >= 0.9.0
Requires:         R-CRAN-shinydashboard >= 0.7.0

%description
Draw geospatial objects by clicks on the map. This packages can help data
analyst who want to check their own geospatial hypothesis but has no
ready-made geospatial objects.

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
