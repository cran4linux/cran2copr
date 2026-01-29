%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggsem
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Structural Equation Modeling (SEM) and Multi-Group Path Diagrams

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-semPlot >= 1.1.7
BuildRequires:    R-CRAN-lavaan >= 0.6.21
BuildRequires:    R-CRAN-blavaan 
BuildRequires:    R-CRAN-DiagrammeRsvg 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-smplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidySEM 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-semPlot >= 1.1.7
Requires:         R-CRAN-lavaan >= 0.6.21
Requires:         R-CRAN-blavaan 
Requires:         R-CRAN-DiagrammeRsvg 
Requires:         R-CRAN-dplyr 
Requires:         R-grDevices 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-network 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-smplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidySEM 
Requires:         R-CRAN-umap 
Requires:         R-CRAN-xml2 

%description
Provides an interactive workflow for visualizing structural equation
modeling (SEM), multi-group path diagrams, and network diagrams in R.
Users can directly manipulate nodes and edges to create
publication-quality figures while maintaining statistical model integrity.
Supports integration with 'lavaan', 'OpenMx', 'tidySEM', and 'blavaan'
etc. Features include parameter-based aesthetic mapping, generative AI
assistance, and complete reproducibility by exporting metadata for
script-based workflows.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
