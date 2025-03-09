%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scRNAstat
%global packver   0.1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Pipeline to Process Single Cell RNAseq Data

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-clustree 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-Seurat 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-clustree 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-patchwork 

%description
A pipeline that can process single or multiple Single Cell RNAseq samples
primarily specializes in Clustering and Dimensionality Reduction.
Meanwhile we use common cell type marker genes for T cells, B cells,
Myeloid cells, Epithelial cells, and stromal cells (Fiboblast, Endothelial
cells, Pericyte, Smooth muscle cells) to visualize the Seurat clusters, to
facilitate labeling them by biological names. Once users named each
cluster, they can evaluate the quality of them again and find the de novo
marker genes also.

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
