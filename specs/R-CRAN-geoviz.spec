%global packname  geoviz
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}
Summary:          Elevation and GPS Data Visualisation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-slippymath 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-png 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-slippymath 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-progress 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgdal 

%description
Simpler processing of digital elevation model and GPS trace data for use
with the 'rayshader' package.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
