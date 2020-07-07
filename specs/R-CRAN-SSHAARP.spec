%global packname  SSHAARP
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Searching Shared HLA Amino Acid Residue Prevalence

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-BIGDAWG 
BuildRequires:    R-CRAN-gmt 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sessioninfo 
BuildRequires:    R-CRAN-filesstrings 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-BIGDAWG 
Requires:         R-CRAN-gmt 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sessioninfo 
Requires:         R-CRAN-filesstrings 

%description
Processes amino acid alignments produced by the 'IPD-IMGT/HLA (Immuno
Polymorphism-ImMunoGeneTics/Human Leukocyte Antigen) Database' to identify
user-defined amino acid residue motifs shared across HLA alleles, and
calculates the frequencies of those motifs based on HLA allele frequency
data. 'SSHAARP' (Searching Shared HLA Amino Acid Residue Prevalence) uses
'Generic Mapping Tools (GMT)' software and the 'GMT' R package to generate
global frequency heat maps that illustrate the distribution of each
user-defined map around the globe. 'SSHAARP' analyzes the allele frequency
data described by Solberg et al. (2008)
<doi:10.1016/j.humimm.2008.05.001>, a global set of 497 population samples
from 185 published datasets, representing 66,800 individuals total.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
