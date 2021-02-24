%global packname  dyngen
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Multi-Modal Simulator for Spearheading Single-Cell Omics Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggraph >= 2.0
BuildRequires:    R-CRAN-dynutils >= 1.0.4
BuildRequires:    R-CRAN-rlang >= 0.4.1
BuildRequires:    R-CRAN-GillespieSSA2 >= 0.2.6
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lmds 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-ggraph >= 2.0
Requires:         R-CRAN-dynutils >= 1.0.4
Requires:         R-CRAN-rlang >= 0.4.1
Requires:         R-CRAN-GillespieSSA2 >= 0.2.6
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lmds 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-viridis 

%description
A novel, multi-modal simulation engine for studying dynamic cellular
processes at single-cell resolution. 'dyngen' is more flexible than
current single-cell simulation engines. It allows better method
development and benchmarking, thereby stimulating development and testing
of novel computational methods. Cannoodt et al. (2020)
<doi:10.1101/2020.02.06.936971>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
