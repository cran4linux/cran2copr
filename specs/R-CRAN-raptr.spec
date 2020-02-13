%global packname  raptr
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Representative and Adequate Prioritization Toolkit in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-hypervolume >= 2.0.7
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-Matrix 
BuildRequires:    R-boot 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-PBSmapping 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-adehabitatHR 
BuildRequires:    R-CRAN-RgoogleMaps 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-gdalUtils 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-hypervolume >= 2.0.7
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-assertthat 
Requires:         R-Matrix 
Requires:         R-boot 
Requires:         R-grDevices 
Requires:         R-CRAN-PBSmapping 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-adehabitatHR 
Requires:         R-CRAN-RgoogleMaps 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-plyr 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-gdalUtils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 

%description
Biodiversity is in crisis. The overarching aim of conservation is to
preserve biodiversity patterns and processes. To this end, protected areas
are established to buffer species and preserve biodiversity processes. But
resources are limited and so protected areas must be cost-effective. This
package contains tools to generate plans for protected areas
(prioritizations), using spatially explicit targets for biodiversity
patterns and processes. To obtain solutions in a feasible amount of time,
this package uses the commercial 'Gurobi' software package (obtained from
<http://www.gurobi.com/>). For more information on using this package, see
Hanson et al. (2018) <doi:10.1111/2041-210X.12862>.

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
%{rlibdir}/%{packname}/libs
