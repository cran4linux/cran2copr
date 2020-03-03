%global packname  seqminer
%global packver   8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.0
Release:          1%{?dist}
Summary:          Efficiently Read Sequence Data (VCF Format, BCF Format, METALFormat and BGEN Format) into R

License:          GPL | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    zlib-devel
BuildRequires:    make,
BuildRequires:    R-devel
Requires:         R-core

%description
Integrate sequencing data (Variant call format, e.g. VCF or BCF) or
meta-analysis results in R. This package can help you (1) read
VCF/BCF/BGEN files by chromosomal ranges (e.g. 1:100-200); (2) read
RareMETAL summary statistics files; (3) read tables from a tabix-indexed
files; (4) annotate VCF/BCF files; (5) create customized workflow based on
Makefile.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bgen
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/plink
%doc %{rlibdir}/%{packname}/rvtests
%doc %{rlibdir}/%{packname}/tabanno
%doc %{rlibdir}/%{packname}/test-triallelic
%doc %{rlibdir}/%{packname}/tests
%doc %{rlibdir}/%{packname}/vcf
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
