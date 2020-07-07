%global packname  leaflet.extras
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Extra Functionality for 'leaflet' Package

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.0
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-leaflet >= 2.0.0
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 

%description
The 'leaflet' JavaScript library provides many plugins some of which are
available in the core 'leaflet' package, but there are many more. It is
not possible to support them all in the core 'leaflet' package. This
package serves as an add-on to the 'leaflet' package by providing extra
functionality via 'leaflet' plugins.

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
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
