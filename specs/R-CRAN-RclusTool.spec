%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RclusTool
%global packver   0.91.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.91.5
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Toolbox for Clustering and Classification of Data Frames

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-conclust 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-CRAN-mmand 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-SearchTrees 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-tkrplot 
Requires:         R-CRAN-class 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-conclust 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mda 
Requires:         R-CRAN-mmand 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-png 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-SearchTrees 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-tools 

%description
Graphical toolbox for clustering and classification of data frames. It
proposes a graphical interface to process clustering and classification
methods on features data-frames, and to view initial data as well as
resulted cluster or classes. According to the level of available labels,
different approaches are proposed: unsupervised clustering,
semi-supervised clustering and supervised classification. To assess the
processed clusters or classes, the toolbox can import and show some
supplementary data formats: either profile/time series, or images. These
added information can help the expert to label clusters (clustering), or
to constrain data frame rows (semi-supervised clustering), using
Constrained spectral embedding algorithm by Wacquet et al. (2013)
<doi:10.1016/j.patrec.2013.02.003> and the methodology provided by Wacquet
et al. (2013) <doi:10.1007/978-3-642-35638-4_21>.

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
