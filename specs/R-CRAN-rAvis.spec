%global packname  rAvis
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}
Summary:          Interface to the Bird-Watching Dataset Proyecto AVIS

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-scrapeR 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-tools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-scrapeR 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-tools 

%description
Interface to <http://proyectoavis.com> database. It provides means to
download data filtered by species, order, family, and several other
criteria. Provides also basic functionality to plot exploratory maps of
the datasets.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/assets
%doc %{rlibdir}/%{packname}/tif
%{rlibdir}/%{packname}/INDEX
