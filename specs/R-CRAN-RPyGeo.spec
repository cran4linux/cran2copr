%global __brp_check_rpaths %{nil}
%global packname  RPyGeo
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          ArcGIS Geoprocessing via Python

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.2
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-reticulate >= 1.2
Requires:         R-CRAN-sf 
Requires:         R-CRAN-raster 
Requires:         R-tools 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-purrr 

%description
Provides access to ArcGIS geoprocessing tools by building an interface
between R and the ArcPy Python side-package via the reticulate package.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
