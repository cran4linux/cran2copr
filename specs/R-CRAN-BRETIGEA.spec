%global packname  BRETIGEA
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Brain Cell Type Specific Gene Expression Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch

%description
Analysis of relative cell type proportions in bulk gene expression data.
Provides a well-validated set of brain cell type-specific marker genes
derived from multiple types of experiments, as described in McKenzie
(2018) <doi:10.1038/s41598-018-27293-5>. For brain tissue data sets, there
are marker genes available for astrocytes, endothelial cells, microglia,
neurons, oligodendrocytes, and oligodendrocyte precursor cells, derived
from each of human, mice, and combination human/mouse data sets. However,
if you have access to your own marker genes, the functions can be applied
to bulk gene expression data from any tissue. Also implements multiple
options for relative cell type proportion estimation using these marker
genes, adapting and expanding on approaches from the 'CellCODE' R package
described in Chikina (2015) <doi:10.1093/bioinformatics/btv015>. The
number of cell type marker genes used in a given analysis can be increased
or decreased based on your preferences and the data set. Finally, provides
functions to use the estimates to adjust for variability in the relative
proportion of cell types across samples prior to downstream analyses.

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
