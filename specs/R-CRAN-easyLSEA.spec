%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easyLSEA
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Lipid Set Enrichment Analysis with Dual KS and 'fgsea' Engines

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-withr 

%description
Provides biology-aware lipid set enrichment analysis (LSEA) for lipidomics
data using dual engines: the Kolmogorov-Smirnov test and the fast gene set
enrichment algorithm from the 'fgsea' package. Annotates lipids into
biological groups at three levels (lipid class, LIPID MAPS category,
functional category) and tests for coordinated directional shifts between
conditions. Includes fatty acid chain analysis with trend plots weighted
by lipid abundance (Spearman rank correlation, configurable smoothing),
wide-format chain position output (sn-1, sn-2, sn-3, sn-4), annotation
confidence filtering, and export utilities for reproducible reporting in
CSV, 'Excel', and PDF formats. Vignettes are available in English and
Spanish. Methods are based on Subramanian et al. (2005)
<doi:10.1073/pnas.0506580102> and Korotkevich et al. (2021)
<doi:10.1101/060012>.

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
