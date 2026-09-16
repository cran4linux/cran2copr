%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FCtools
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Connectivity Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggplotify 
Requires:         R-CRAN-ggraph 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-png 
Requires:         R-CRAN-reshape2 

%description
Analyzing and visualizing brain connectivity data, including network-based
statistics (NBS) for linear and linear mixed models, both at edge level
and functional network level (Yeo's 7-networks (Schaefer et al. (2017)
<doi:10.1093/cercor/bhx179>)). Plots include edge-wise connectograms,
chord diagrams, network connectograms, heatmaps, and 3D glass brain
connectivity plots. 'FCtools' works with vectors of edges (derived from
connectivity/adjacency matrices) from the 'Brainnetome' (Fan et al. (2016)
<doi:10.1093/cercor/bhw157>), 'Schaefer' (100 or 200, each with 19 'ASeg'
subcortices) (Schaefer et al. (2017) <doi:10.1093/cercor/bhx179>, Fischl
et al. (2002) <doi:10.1016/S0896-6273(02)00569-X>), and 'Automated
Anatomical Labeling' (AAL) atlases (Tzourio-Mazoyer et al. (2002)
<doi:10.1006/nimg.2001.0978>).

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
