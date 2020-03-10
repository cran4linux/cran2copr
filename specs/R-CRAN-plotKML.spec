%global packname  plotKML
%global packver   0.6-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}
Summary:          Visualization of Spatial and Spatio-Temporal Objects in GoogleEarth

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-aqp 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-pixmap 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-RSAGA 
BuildRequires:    R-CRAN-classInt 
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-aqp 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-pixmap 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-RSAGA 
Requires:         R-CRAN-classInt 

%description
Writes sp-class, spacetime-class, raster-class and similar spatial and
spatio-temporal objects to KML following some basic cartographic rules.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/eberg.xml
%doc %{rlibdir}/%{packname}/FGDC.xml
%doc %{rlibdir}/%{packname}/gpx.xsd
%doc %{rlibdir}/%{packname}/INSPIRE_ISO19139.xml
%doc %{rlibdir}/%{packname}/mdnames.csv
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/ogckml22.xsd
%{rlibdir}/%{packname}/INDEX
