%global packname  plinkQC
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Genotype Quality Control with 'PLINK'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 1.2.4
BuildRequires:    R-CRAN-data.table >= 1.11.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-optparse 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-UpSetR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sys 
Requires:         R-CRAN-igraph >= 1.2.4
Requires:         R-CRAN-data.table >= 1.11.0
Requires:         R-methods 
Requires:         R-CRAN-optparse 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-UpSetR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sys 

%description
Genotyping arrays enable the direct measurement of an individuals genotype
at thousands of markers. 'plinkQC' facilitates genotype quality control
for genetic association studies as described by Anderson and colleagues
(2010) <doi:10.1038/nprot.2010.116>. It makes 'PLINK' basic statistics
(e.g. missing genotyping rates per individual, allele frequencies per
genetic marker) and relationship functions accessible from 'R' and
generates a per-individual and per-marker quality control report.
Individuals and markers that fail the quality control can subsequently be
removed to generate a new, clean dataset. Removal of individuals based on
relationship status is optimised to retain as many individuals as possible
in the study.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
