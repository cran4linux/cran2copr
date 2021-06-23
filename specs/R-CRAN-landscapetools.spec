%global __brp_check_rpaths %{nil}
%global packname  landscapetools
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}%{?buildtag}
Summary:          Landscape Utility Toolbox

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-Rcpp 

%description
Provides utility functions for some of the less-glamorous tasks involved
in landscape analysis. It includes functions to coerce raster data to the
common tibble format and vice versa, it helps with flexible
reclassification tasks of raster data and it provides a function to merge
multiple raster. Furthermore, 'landscapetools' helps landscape scientists
to visualize their data by providing optional themes and utility functions
to plot single landscapes, rasterstacks, -bricks and lists of raster.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
