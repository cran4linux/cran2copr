%global packname  birdring
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          3%{?dist}
Summary:          Methods to Analyse Ring Re-Encounter Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.1
Requires:         R-core >= 2.10.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-lazyData 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rworldmap 
BuildRequires:    R-CRAN-rworldxtra 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-lazyData 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rworldmap 
Requires:         R-CRAN-rworldxtra 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-graphics 

%description
R functions to read EURING data and analyse re-encounter data of birds
marked by metal rings. For a tutorial, go to
<http://www.tandfonline.com/doi/full/10.1080/03078698.2014.933053>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
