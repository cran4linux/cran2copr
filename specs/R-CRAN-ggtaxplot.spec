%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggtaxplot
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Create Plots to Visualize Taxonomy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-ggalluvial 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-ggalluvial 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 

%description
Provides a comprehensive suite of functions for processing and visualizing
taxonomic data. It includes functionality to clean and transform taxonomic
data, categorize it into hierarchical ranks (such as Phylum, Class, Order,
Family, and Genus), and calculate the relative abundance of each category.
The package also generates a color palette for visual representation of
the taxonomic data, allowing users to easily identify and differentiate
between various taxonomic groups. Additionally, it features a river plot
visualization to effectively display the distribution of individuals
across different taxonomic ranks, facilitating insights into taxonomic
visualization.

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
