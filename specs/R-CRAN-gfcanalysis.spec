%global packname  gfcanalysis
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          2%{?dist}%{?buildtag}
Summary:          Tools for Working with Hansen et al. Global Forest ChangeDataset

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-rasterVis 
Requires:         R-CRAN-raster 
Requires:         R-methods 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-rasterVis 

%description
Supports analyses using the Global Forest Change dataset released by
Hansen et al. gfcanalysis was originally written for the Tropical Ecology
Assessment and Monitoring (TEAM) Network. For additional details on the
Global Forest Change dataset, see: Hansen, M. et al. 2013.
"High-Resolution Global Maps of 21st-Century Forest Cover Change." Science
342 (15 November): 850-53. The forest change data and more information on
the product is available at <http://earthenginepartners.appspot.com>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
