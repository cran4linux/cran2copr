%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HVT
%global packver   25.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          25.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Constructing Hierarchical Voronoi Tessellations and Overlay Heatmaps for Data Analysis

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-NbClust 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-markovchain 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-MASS 
Requires:         R-grDevices 
Requires:         R-CRAN-splancs 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-NbClust 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-umap 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-markovchain 
Requires:         R-methods 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-gridExtra 

%description
Facilitates building topology preserving maps for data analysis.

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
