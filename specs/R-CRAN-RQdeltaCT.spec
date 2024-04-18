%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RQdeltaCT
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Relative Quantification of Gene Expression using Delta Ct Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-ctrlGene 
BuildRequires:    R-CRAN-ggsignif 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-ggpmisc 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-oddsratio 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-GGally 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-ctrlGene 
Requires:         R-CRAN-ggsignif 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-ggpmisc 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-oddsratio 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-GGally 

%description
The commonly used methods for relative quantification of gene expression
levels obtained in real-time PCR (Polymerase Chain Reaction) experiments
are the delta Ct methods, encompassing 2^-dCt and 2^-ddCt methods,
originally proposed by Kenneth J. Livak and Thomas D. Schmittgen (2001)
<doi:10.1006/meth.2001.1262>. The main idea is to normalise gene
expression values using endogenous control gene, present gene expression
levels in linear form by using the 2^-(value)^ transformation, and
calculate differences in gene expression levels between groups of samples
(or technical replicates of a single sample). The 'RQdeltaCT' package
offers functions that cover both methods for comparison of either
independent groups of samples or groups with paired samples, together with
importing expression datasets, performing multi-step quality control of
data, enabling numerous data visualisations, enrichment of the standard
workflow with additional useful analyses (correlation analysis, Receiver
Operating Characteristic analysis, logistic regression), and conveniently
export obtained results in table and image formats. The package has been
designed to be friendly to non-experts in R programming.

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
