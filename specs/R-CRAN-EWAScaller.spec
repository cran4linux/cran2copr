%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EWAScaller
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Query and Analyse the 'EWAS Atlas' Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggwordcloud 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-digest 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggwordcloud 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a client for the 'EWAS Atlas' web services
(<https://ngdc.cncb.ac.cn/ewas/>; Li et al. (2019)
<doi:10.1093/nar/gky1027>), allowing users to query epigenome-wide
association study (EWAS) data by CpG (cytosine-phosphate-guanine) probe
identifier, gene symbol, or genomic region, and to run trait, Gene
Ontology, KEGG (Kyoto Encyclopedia of Genes and Genomes) pathway, and
genomic location enrichment analyses on a set of CpG probes. Query
functions support concurrent, rate-limited requests to the remote service.
Results are returned as tidy data frames with dedicated summary and
plotting methods, including word clouds of enriched 'EWAS Atlas' trait
terms.

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
