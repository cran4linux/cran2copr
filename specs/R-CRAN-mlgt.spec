%global packname  mlgt
%global packver   0.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16
Release:          2%{?dist}
Summary:          Multi-Locus Geno-Typing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-seqinr 
Requires:         R-methods 
Requires:         R-CRAN-seqinr 

%description
Processing and analysis of high throughput (Roche 454) sequences generated
from multiple loci and multiple biological samples. Sequences are assigned
to their locus and sample of origin, aligned and trimmed. Where possible,
genotypes are called and variants mapped to known alleles.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/HLA_intersectMarkersDec11.fasta
%doc %{rlibdir}/%{packname}/HLA_namedMarkers.fasta
%doc %{rlibdir}/%{packname}/marker.imgt.msf.list.tab
%doc %{rlibdir}/%{packname}/namedBarcodes.fasta
%doc %{rlibdir}/%{packname}/namedBarcodesFull.fasta
%doc %{rlibdir}/%{packname}/sampleSequences.fasta
%doc %{rlibdir}/%{packname}/tableOfSampleBarcodeMapping.tab
%{rlibdir}/%{packname}/INDEX
