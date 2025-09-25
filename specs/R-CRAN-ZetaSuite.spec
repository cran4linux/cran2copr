%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ZetaSuite
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze High-Dimensional High-Throughput Dataset and Quality Control Single-Cell RNA-Seq

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-DT 

%description
The advent of genomic technologies has enabled the generation of
two-dimensional or even multi-dimensional high-throughput data, e.g.,
monitoring multiple changes in gene expression in genome-wide siRNA
screens across many different cell types (E Robert McDonald 3rd (2017)
<doi: 10.1016/j.cell.2017.07.005> and Tsherniak A (2017) <doi:
10.1016/j.cell.2017.06.010>) or single cell transcriptomics under
different experimental conditions. We found that simple computational
methods based on a single statistical criterion is no longer adequate for
analyzing such multi-dimensional data. We herein introduce 'ZetaSuite', a
statistical package initially designed to score hits from two-dimensional
RNAi screens.We also illustrate a unique utility of 'ZetaSuite' in
analyzing single cell transcriptomics to differentiate rare cells from
damaged ones (Vento-Tormo R (2018) <doi: 10.1038/s41586-018-0698-6>). In
'ZetaSuite', we have the following steps: QC of input datasets,
normalization using Z-transformation, Zeta score calculation and hits
selection based on defined Screen Strength.

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
