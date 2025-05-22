%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  doblin
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          'doblin': Inferring Dominant Clonal Lineages from DNA Barcoding Time-Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-imputeTS 
BuildRequires:    R-CRAN-dtwclust 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-TSdist 
BuildRequires:    R-graphics 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-proxy 
Requires:         R-grid 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-reshape2 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-imputeTS 
Requires:         R-CRAN-dtwclust 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-TSdist 
Requires:         R-graphics 

%description
Provides functions to quantify dominant clonal lineages from DNA barcoding
time-series data. The package implements clustering of barcode lineage
trajectories, based on the assumption that similar temporal dynamics
indicate comparable relative fitness. It also identifies persistent clonal
lineages across time points. Input data can include lineage frequency
tables derived from chromosomal barcoding, mutational libraries, or
CRISPR/Cas screens. For more details, see Gagné-Leroux et al. (2024)
<doi:10.1101/2024.09.08.611892>.

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
