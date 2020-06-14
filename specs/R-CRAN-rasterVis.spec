%global packname  rasterVis
%global packver   0.47
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.47
Release:          2%{?dist}
Summary:          Visualization Methods for Raster Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.0.12
BuildRequires:    R-CRAN-sp >= 1.0.6
BuildRequires:    R-methods 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-raster >= 2.0.12
Requires:         R-CRAN-sp >= 1.0.6
Requires:         R-methods 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-viridisLite 

%description
Methods for enhanced visualization and interaction with raster data. It
implements visualization methods for quantitative data and categorical
data, both for univariate and multivariate rasters. It also provides
methods to display spatiotemporal rasters, and vector fields. See the
website for examples.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
