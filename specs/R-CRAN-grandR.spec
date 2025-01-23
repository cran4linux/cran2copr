%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  grandR
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Analysis of Nucleotide Conversion Sequencing Data

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-lfc 
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-plyr 
Requires:         R-parallel 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-lfc 
Requires:         R-CRAN-labeling 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-numDeriv 

%description
Nucleotide conversion sequencing experiments have been developed to add a
temporal dimension to RNA-seq and single-cell RNA-seq. Such experiments
require specialized tools for primary processing such as GRAND-SLAM, (see
'Jürges et al' <doi:10.1093/bioinformatics/bty256>) and specialized tools
for downstream analyses. 'grandR' provides a comprehensive toolbox for
quality control, kinetic modeling, differential gene expression analysis
and visualization of such data.

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
