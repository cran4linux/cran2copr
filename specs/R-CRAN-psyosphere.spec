%global packname  psyosphere
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Analyse GPS Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-RgoogleMaps 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-RgoogleMaps 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 

%description
Analyse location data such as latitude, longitude, and elevation. Based on
spherical trigonometry, variables such as speed, bearing, and distances
can be calculated from moment to moment, depending on the sampling
frequency of the equipment used, and independent of scale. Additionally,
the package can plot tracks, coordinates, and shapes on maps, and
sub-tracks can be selected with point-in-polygon or other techniques. The
package is optimized to support behavioural science experiments with
multiple tracks. It can detect and clean up errors in the data, and
resulting data can be exported to be analysed in statistical software or
geographic information systems (GIS).

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
