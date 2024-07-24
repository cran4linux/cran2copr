%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WormTensor
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Clustering Method for Time-Series Whole-Brain Activity Data of 'C. elegans'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-usedist 
BuildRequires:    R-CRAN-dtwclust 
BuildRequires:    R-CRAN-clusterSim 
BuildRequires:    R-CRAN-clValid 
BuildRequires:    R-CRAN-aricode 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-methods 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-usedist 
Requires:         R-CRAN-dtwclust 
Requires:         R-CRAN-clusterSim 
Requires:         R-CRAN-clValid 
Requires:         R-CRAN-aricode 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-cowplot 
Requires:         R-methods 

%description
A toolkit to detect clusters from distance matrices. The distance matrices
are assumed to be calculated between the cells of multiple animals
('Caenorhabditis elegans') from input time-series matrices. Some functions
for generating distance matrices, performing clustering, evaluating the
clustering, and visualizing the results of clustering and evaluation are
available. We're also providing the download function to retrieve the
calculated distance matrices from 'figshare' <https://figshare.com>.

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
