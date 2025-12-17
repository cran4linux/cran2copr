%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SuperCell
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simplification of scRNA-Seq Data by Merging Together Similar Cells

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-plotfunctions 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-weights 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-irlba 
Requires:         R-grDevices 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-umap 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-plotfunctions 
Requires:         R-CRAN-proxy 
Requires:         R-methods 
Requires:         R-CRAN-rlang 

%description
Aggregates large single-cell data into metacell dataset by merging
together gene expression of very similar cells. 'SuperCell' uses
'velocyto.R' <doi:10.1038/s41586-018-0414-6>
<https://github.com/velocyto-team/velocyto.R> for RNA velocity and
'WeightedCluster' <doi:10.12682/lives.2296-1658.2013.24>
<https://mephisto.unige.ch/weightedcluster/> for weighted clustering on
metacells. We also recommend installing 'scater' Bioconductor package
<doi:10.18129/B9.bioc.scater>
<https://bioconductor.org/packages/release/bioc/html/scater.html>.

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
