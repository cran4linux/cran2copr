%global debug_package %{nil}
%global packname  reproducible
%global packver   0.2.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.11
Release:          1%{?dist}
Summary:          A Set of Tools that Enhance Reproducibility Beyond PackageManagement

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-archivist >= 2.1.2
BuildRequires:    R-CRAN-RCurl >= 1.95.4.8
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-git2r >= 0.18
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fastdigest 
BuildRequires:    R-CRAN-fasterize 
BuildRequires:    R-CRAN-fpCompare 
BuildRequires:    R-CRAN-gdalUtils 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-quickPlot 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-versions 
Requires:         R-CRAN-archivist >= 2.1.2
Requires:         R-CRAN-RCurl >= 1.95.4.8
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-git2r >= 0.18
Requires:         R-CRAN-backports 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fastdigest 
Requires:         R-CRAN-fasterize 
Requires:         R-CRAN-fpCompare 
Requires:         R-CRAN-gdalUtils 
Requires:         R-CRAN-googledrive 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-quickPlot 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-testthat 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-versions 

%description
Collection of high-level, robust, machine- and OS-independent tools for
making deeply reproducible and reusable content in R. This includes light
weight package management (similar to 'packrat' and 'checkpoint', but more
flexible, lightweight, simpler yet less tested than both), tools for
caching, downloading and verifying or writing checksums, post-processing
of common spatial datasets, and accessing GitHub repositories. Some
features are still under active development.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
