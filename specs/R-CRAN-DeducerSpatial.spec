%global packname  DeducerSpatial
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          2%{?dist}
Summary:          Deducer for spatial data analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Deducer >= 0.7.4
BuildRequires:    R-CRAN-JavaGD >= 0.6.0
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-OpenStreetMap 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-UScensus2010 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-Deducer >= 0.7.4
Requires:         R-CRAN-JavaGD >= 0.6.0
Requires:         R-CRAN-sp 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-OpenStreetMap 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-UScensus2010 
Requires:         R-CRAN-Hmisc 

%description
A Deducer plug-in for spatial data analysis. Includes The ability to plot
and explore open street map and Bing satellite images.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
