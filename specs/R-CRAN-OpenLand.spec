%global packname  OpenLand
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Quantitative Analysis and Visualization of LUCC

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-raster >= 3.0.7
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-circlize >= 0.4.8
BuildRequires:    R-CRAN-networkD3 >= 0.4
BuildRequires:    R-grid 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-raster >= 3.0.7
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-circlize >= 0.4.8
Requires:         R-CRAN-networkD3 >= 0.4
Requires:         R-grid 
Requires:         R-methods 

%description
Tools for the analysis of land use and cover (LUC) time series. It
includes support for loading spatiotemporal raster data and synthesized
spatial plotting. Several LUC change (LUCC) metrics in regular or
irregular time intervals can be extracted and visualized through one- and
multistep sankey and chord diagrams. A complete intensity analysis
according to Aldwaik and Pontius (2012)
<doi:10.1016/j.landurbplan.2012.02.010> is implemented, including tools
for the generation of standardized multilevel output graphics.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
