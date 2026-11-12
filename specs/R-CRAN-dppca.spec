%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dppca
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Differentially Private Principal Component Analysis and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-VGAM 

%description
Provides tools for differentially private principal component analysis
(PCA) and visualization. Includes private principal component directions,
scree and proportion of variance explained (PVE) estimates, and
two-dimensional private score histograms with synthetic sampled points.
Supports additive and sparse histogram mechanisms, group-wise score
visualizations, and optional non-private comparisons. An integrated
workflow produces loading plots, scree plots, score plots, variable plots,
and biplots from shared private PCA estimates. An interactive 'shiny'
application is also provided. Private direction estimation is based on Kim
and Jung (2025) <doi:10.1002/sam.70053>. Private scree estimation draws on
Dwork and Roth (2014) <doi:10.1561/0400000042>, Ramsay and Spicker (2025)
<doi:10.48550/arXiv.2501.14095>, and Yu, Ren and Zhou (2024)
<doi:10.3150/23-BEJ1706>. Private score frames use unbounded quantile
mechanisms from Durfee (2023) <doi:10.52202/075280-3394>. Private score
histograms use methods related to Wasserman and Zhou (2010)
<doi:10.1198/jasa.2009.tm08651> and Karwa and Vadhan (2018)
<doi:10.4230/LIPIcs.ITCS.2018.44>.

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
