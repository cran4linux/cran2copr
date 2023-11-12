%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AnanseSeurat
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Construct ANANSE GRN-Analysis Seurat

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.50
Requires:         R-core >= 3.50
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-png 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Seurat 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Enables gene regulatory network (GRN) analysis on single cell clusters,
using the GRN analysis software 'ANANSE', Xu et al.(2021)
<doi:10.1093/nar/gkab598>. Export data from 'Seurat' objects, for GRN
analysis by 'ANANSE' implemented in 'snakemake'. Finally, incorporate
results for visualization and interpretation.

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
