%global packname  pagoda2
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Single Cell Analysis and Differential Expression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-sccore >= 0.1.1
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-dendsort 
BuildRequires:    R-CRAN-drat 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-N2R 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RMTstat 
BuildRequires:    R-CRAN-Rook 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-sccore >= 0.1.1
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-dendsort 
Requires:         R-CRAN-drat 
Requires:         R-CRAN-fastcluster 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mgcv 
Requires:         R-methods 
Requires:         R-CRAN-N2R 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-RMTstat 
Requires:         R-CRAN-Rook 
Requires:         R-CRAN-Rtsne 
Requires:         R-stats 
Requires:         R-CRAN-urltools 
Requires:         R-utils 

%description
Analyzing and interactively exploring large-scale single-cell RNA-seq
datasets. 'pagoda2' primarily performs normalization and differential gene
expression analysis, with an interactive application for exploring
single-cell RNA-seq datasets. It performs basic tasks such as cell size
normalization, gene variance normalization, and can be used to identify
subpopulations and run differential expression within individual samples.
'pagoda2' was written to rapidly process modern large-scale scRNAseq
datasets of approximately 1e6 cells. The companion web application allows
users to explore which gene expression patterns form the different
subpopulations within your data. The package also serves as the primary
method for preprocessing data for conos,
<https://github.com/kharchenkolab/conos>. This package interacts with data
available through the 'p2data' package, which is available in a 'drat'
repository. To access this data package, see the instructions at
<https://github.com/kharchenkolab/pagoda2>. The size of the 'p2data'
package is approximately 6 MB.

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
