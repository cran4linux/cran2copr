%global packname  semnar
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          2%{?dist}
Summary:          Constructing and Interacting with Databases of Presentations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-urlshorteneR 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-urlshorteneR 

%description
Provides methods for constructing and maintaining a database of
presentations in R. The presentations are either ones that the user gives
or gave or presentations at a particular event or event series. The
package also provides a plot method for the interactive mapping of the
presentations using 'leaflet' by grouping them according to country, city,
year and other presentation attributes. The markers on the map come with
popups providing presentation details (title, institution, event, links to
materials and events, and so on).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/art
%{rlibdir}/%{packname}/INDEX
