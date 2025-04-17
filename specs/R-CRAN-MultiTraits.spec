%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiTraits
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing and Visualizing Multidimensional Plant Traits

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtern 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtern 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-ggrepel 

%description
Implements analytical methods for multidimensional plant traits, including
Competitors-Stress tolerators-Ruderals strategy analysis using leaf
traits, Leaf-Height-Seed strategy analysis, Niche Periodicity Table
analysis, and Trait Network analysis. Provides functions for data
analysis, visualization, and network metrics calculation. Methods are
based on Grime (1974) <doi:10.1038/250026a0>, Pierce et al. (2017)
<doi:10.1111/1365-2435.12882>, Westoby (1998)
<doi:10.1023/A:1004327224729>, Yang et al. (2022)
<doi:10.1016/j.foreco.2022.120540>, Winemiller et al. (2015)
<doi:10.1111/ele.12462>, He et al. (2020)
<doi:10.1016/j.tree.2020.06.003>.

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
