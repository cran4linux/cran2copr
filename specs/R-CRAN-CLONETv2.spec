%global packname  CLONETv2
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          2%{?dist}
Summary:          Clonality Estimates in Tumor

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-arules 
Requires:         R-parallel 
Requires:         R-CRAN-sets 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-arules 

%description
Analyze data from next-generation sequencing experiments on genomic
samples. 'CLONETv2' offers a set of functions to compute allele specific
copy number and clonality from segmented data and SNPs position pileup.
The package has also calculated the clonality of single nucleotide
variants given read counts at mutated positions. The package has been
developed at the laboratory of Computational and Functional Oncology,
Department of CIBIO, University of Trento (Italy), under the supervision
of prof Francesca Demichelis. References: Prandi et al. (2014)
<doi:10.1186/s13059-014-0439-6>; Carreira et al. (2014)
<doi:10.1126/scitranslmed.3009448>.

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
%doc %{rlibdir}/%{packname}/sample_normal_pileup.tsv
%doc %{rlibdir}/%{packname}/sample_snv_read_count.tsv
%doc %{rlibdir}/%{packname}/sample_tumor_pileup.tsv
%doc %{rlibdir}/%{packname}/sample.seg
%doc %{rlibdir}/%{packname}/sample1_normal_pileup.tsv.gz
%doc %{rlibdir}/%{packname}/sample1_snv_read_count.tsv
%doc %{rlibdir}/%{packname}/sample1_tumor_pileup.tsv.gz
%doc %{rlibdir}/%{packname}/sample1.seg
%doc %{rlibdir}/%{packname}/sample2_normal_pileup.tsv.gz
%doc %{rlibdir}/%{packname}/sample2_snv_read_count.tsv
%doc %{rlibdir}/%{packname}/sample2_tumor_pileup.tsv.gz
%doc %{rlibdir}/%{packname}/sample2.seg
%doc %{rlibdir}/%{packname}/sample3_normal_pileup.tsv.gz
%doc %{rlibdir}/%{packname}/sample3_snv_read_count.tsv
%doc %{rlibdir}/%{packname}/sample3_tumor_pileup.tsv.gz
%doc %{rlibdir}/%{packname}/sample3.seg
%doc %{rlibdir}/%{packname}/sample4_normal_pileup.tsv.gz
%doc %{rlibdir}/%{packname}/sample4_snv_read_count.tsv
%doc %{rlibdir}/%{packname}/sample4_tumor_pileup.tsv.gz
%doc %{rlibdir}/%{packname}/sample4.seg
%doc %{rlibdir}/%{packname}/sample5_normal_pileup.tsv.gz
%doc %{rlibdir}/%{packname}/sample5_snv_read_count.tsv
%doc %{rlibdir}/%{packname}/sample5_tumor_pileup.tsv.gz
%doc %{rlibdir}/%{packname}/sample5.seg
%{rlibdir}/%{packname}/INDEX
