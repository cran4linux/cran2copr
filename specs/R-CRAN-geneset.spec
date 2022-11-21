%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geneset
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Get Gene Sets for Gene Enrichment Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-fst 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 

%description
Gene sets are fundamental for gene enrichment analysis. The package
'geneset' enables querying gene sets from public databases including 'GO'
(Gene Ontology Consortium. (2004) <doi:10.1093/nar/gkh036>), 'KEGG'
(Minoru et al. (2000) <doi:10.1093/nar/28.1.27>), 'WikiPathway' (Marvin et
al. (2020) <doi:10.1093/nar/gkaa1024>), 'MsigDb' (Arthur et al. (2015)
<doi:10.1016/j.cels.2015.12.004>), 'Reactome' (David et al. (2011)
<doi:10.1093/nar/gkq1018>), 'MeSH' (Ish et al. (2014)
<doi:10.4103/0019-5413.139827>), 'DisGeNET' (Janet et al. (2017)
<doi:10.1093/nar/gkw943>), 'Disease Ontology' (Lynn et al. (2011)
<doi:10.1093/nar/gkr972>), 'Network of Cancer Genes' (Dimitra et al.
(2019) <doi:10.1186/s13059-018-1612-0>) and 'COVID-19' (Maxim et al.
(2020) <doi:10.21203/rs.3.rs-28582/v1>). Gene sets are stored in the list
object which provides data frame of 'geneset' and 'geneset_name'. The
'geneset' has two columns of term ID and gene ID. The 'geneset_name' has
two columns of terms ID and term description.

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
