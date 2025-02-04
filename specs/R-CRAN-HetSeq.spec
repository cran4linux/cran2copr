%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HetSeq
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Identifying Modulators of Cellular Responses Leveraging Intercellular Heterogeneity

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-DoubleML 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrastr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-grandR 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-stats 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-DoubleML 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrastr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-grandR 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Seurat 
Requires:         R-stats 

%description
Cellular responses to perturbations are highly heterogeneous and depend
largely on the initial state of cells. Connecting post-perturbation cells
via cellular trajectories to untreated cells (e.g. by leveraging metabolic
labeling information) enables exploitation of intercellular heterogeneity
as a combined knock-down and overexpression screen to identify pathway
modulators, termed Heterogeneity-seq (see 'Berg et al'
<doi:10.1101/2024.10.28.620481>). This package contains functions to
generate cellular trajectories based on scSLAM-seq (single-cell,
thiol-(SH)-linked alkylation of RNA for metabolic labelling sequencing)
time courses, functions to identify pathway modulators and to visualize
the results.

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
