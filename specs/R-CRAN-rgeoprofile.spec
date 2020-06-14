%global packname  rgeoprofile
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Geographic Profiling Methods for Serial Crime Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-aspace 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-pals 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-utils 
Requires:         R-CRAN-aspace 
Requires:         R-CRAN-geosphere 
Requires:         R-grDevices 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-pals 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-splancs 
Requires:         R-utils 

%description
An implementation of functions for the analysis of serial crime incidents.
The package implements algorithms for the geographical profiling of serial
incidents in attempt to prioritize the area in which the anchor point or
home base of the perpetrator is located. The geographic profiling methods
in the package are implemented based upon the 'Dragnet' software by
Canter, Coffey, Huntley, and Missen (2000) <doi:10.1023/A:1007551316253>,
the 'CrimeStat' software by Levine (2013)
<https://nij.ojp.gov/topics/articles/crimestat-spatial-statistics-program-analysis-crime-incident-locations>,
and the criminal geographic targeting model outlined in Rossmo (2000,
ISBN:978-0849381294) and Rossmo (1995) <http://summit.sfu.ca/item/6820>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
