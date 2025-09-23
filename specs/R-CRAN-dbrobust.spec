%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dbrobust
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Distance-Based Visualization and Analysis of Mixed-Type Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5
Requires:         R-core >= 4.5
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-dbstats 
BuildRequires:    R-CRAN-StatMatch 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-dbstats 
Requires:         R-CRAN-StatMatch 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-vegan 

%description
Robust distance-based methods applied to matrices and data frames,
producing distance matrices that can be used as input for various
visualization techniques such as graphs, heatmaps, or multidimensional
scaling configurations. See Boj and Grané (2024)
<doi:10.1016/j.seps.2024.101992>.

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
