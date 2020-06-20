%global packname  graph4lg
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Build Graphs for Landscape Genetics Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pegas 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-diveRsity 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-ecodist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-adegenet 
Requires:         R-stats 
Requires:         R-CRAN-spatstat 
Requires:         R-Matrix 
Requires:         R-CRAN-vegan 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-pegas 
Requires:         R-MASS 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-diveRsity 
Requires:         R-CRAN-raster 
Requires:         R-foreign 
Requires:         R-CRAN-ecodist 

%description
Build graphs for landscape genetics analysis. This set of functions can be
used to import and convert spatial and genetic data initially in different
formats, import landscape graphs created with 'GRAPHAB' software (Foltete
et al., 2012) <doi:10.1016/j.envsoft.2012.07.002>, make diagnosis plots of
isolation by distance relationships in order to choose how to build
genetic graphs, create graphs with a large range of pruning methods,
weight their links with several genetic distances, plot and analyse
graphs, compare them with other graphs. It uses functions from other
packages such as 'adegenet' (Jombart, 2008)
<doi:10.1093/bioinformatics/btn129> and 'igraph' (Csardi et Nepusz, 2006)
<https://bit.ly/35a3V3H>. It also implements methods commonly used in
landscape genetics to create graphs, described by Dyer et Nason (2004)
<doi:10.1111/j.1365-294X.2004.02177.x> and Greenbaum et Fefferman (2017)
<doi:10.1111/mec.14059>, and to analyse distance data (van Strien et al.,
2015) <doi:10.1038/hdy.2014.62>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
