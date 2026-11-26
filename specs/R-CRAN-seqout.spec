%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seqout
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Client for Querying the 'Seqout' Genomics Metadata Database

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-curl 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 

%description
Search and download genomics study metadata from 'Seqout'
<https://seqout.org>, through its REST (Representational State Transfer)
web service <https://seqout.org/api/> or its Parquet data dump
<https://seqout.org/data>. 'Seqout' indexes the National Center for
Biotechnology Information (NCBI) Gene Expression Omnibus (GEO)
<https://www.ncbi.nlm.nih.gov/geo/> and Sequence Read Archive (SRA)
<https://www.ncbi.nlm.nih.gov/sra>, the European Bioinformatics Institute
(EBI) European Nucleotide Archive (ENA)
<https://www.ebi.ac.uk/ena/browser/>, the DNA Data Bank of Japan (DDBJ)
Sequence Read Archive (DRA) and Genomic Expression Archive (GEA)
<https://www.ddbj.nig.ac.jp>, ArrayExpress
<https://www.ebi.ac.uk/biostudies/arrayexpress>, and the Genome Sequence
Archive (GSA) <https://ngdc.cncb.ac.cn/gsa/>.

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
