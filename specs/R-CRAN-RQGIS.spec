%global packname  RQGIS
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Integrating R with QGIS

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.2
BuildRequires:    R-CRAN-sf >= 0.4.2
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-reticulate >= 1.2
Requires:         R-CRAN-sf >= 0.4.2
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-CRAN-XML 

%description
Establishes an interface between R and 'QGIS', i.e. it allows the user to
access 'QGIS' functionalities from the R console. It achieves this by
using the 'QGIS' Python API via the command line. Hence, RQGIS extends R's
statistical power by the incredible vast geo-functionality of 'QGIS'
(including also 'GDAL', 'SAGA'- and 'GRASS'-GIS among other third-party
providers). This in turn creates a powerful environment for advanced and
innovative (geo-)statistical geocomputing. 'QGIS' is licensed under GPL
version 2 or greater and is available from <http://www.qgis.org/en/site/>.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/python
%doc %{rlibdir}/%{packname}/test-scripts
%doc %{rlibdir}/%{packname}/travis
%{rlibdir}/%{packname}/INDEX
