%global __brp_check_rpaths %{nil}
%global packname  ActivePathways
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Integrative Pathway Enrichment Analysis of Multivariate Omics Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 

%description
Framework for analysing multiple omics datasets in the context of
molecular pathways, biological processes and other types of gene sets. The
package uses p-value merging to combine gene- or protein-level signals,
followed by ranked hypergeometric tests to determine enriched pathways and
processes. This approach allows researchers to interpret a series of omics
datasets in the context of known biology and gene function, and discover
associations that are only apparent when several datasets are combined.
The package is part of the following publication: Integrative Pathway
Enrichment Analysis of Multivariate Omics Data. Paczkowska M^, Barenboim
J^, Sintupisut N, Fox NS, Zhu H, Abd-Rabbo D, Mee MW, Boutros PC, PCAWG
Drivers and Functional Interpretation Working Group; Reimand J, PCAWG
Consortium. Nature Communications (2020) <doi:10.1038/s41467-019-13983-9>.

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
