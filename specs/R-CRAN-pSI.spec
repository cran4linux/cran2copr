%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pSI
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Specificity Index Statistic

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Calculates the Specificity Index (pSI) statistic, which identifies genes
enriched in specific cell types or tissues from a matrix of expression
profiles, and provides post-processing tools: lists and counts of specific
genes at standard pSI thresholds, overlap with candidate gene lists, and
Fisher's exact tests for enrichment of a candidate gene list across all
cell types and thresholds (Cell type-Specific Expression Analysis, CSEA).
The methods are described in Dougherty et al. (2010)
<doi:10.1093/nar/gkq130>, Xu et al. (2014)
<doi:10.1523/JNEUROSCI.4488-13.2014> and Wells et al. (2015)
<doi:10.1093/nar/gkv1262>. The precomputed pSI tables for mouse cell types
and human brain regions used in those papers, formerly the 'pSI.data'
package, are downloaded on first use with psi_data().

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
