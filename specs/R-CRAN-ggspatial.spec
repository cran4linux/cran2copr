%global packname  ggspatial
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Spatial Data Framework for ggplot2

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1.9000
BuildRequires:    R-CRAN-rosm >= 0.2
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-grid 
Requires:         R-CRAN-ggplot2 >= 2.2.1.9000
Requires:         R-CRAN-rosm >= 0.2
Requires:         R-CRAN-sf 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-reshape2 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-grid 

%description
Spatial data plus the power of the ggplot2 framework means easier mapping
when input data are already in the form of spatial objects.

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
%doc %{rlibdir}/%{packname}/longlake
%doc %{rlibdir}/%{packname}/rosm.cache
%{rlibdir}/%{packname}/INDEX
