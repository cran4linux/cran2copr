%global packname  prewas
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Data Pre-Processing for Bacterial Genome-Wide AssociationStudies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.3
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-utils >= 3.5.0
BuildRequires:    R-methods >= 3.5.0
BuildRequires:    R-CRAN-phangorn >= 2.5.5
BuildRequires:    R-CRAN-vcfR >= 1.8.0
BuildRequires:    R-CRAN-future.apply >= 1.3.0
BuildRequires:    R-CRAN-future >= 1.15.1
Requires:         R-CRAN-ape >= 5.3
Requires:         R-stats >= 3.5.0
Requires:         R-utils >= 3.5.0
Requires:         R-methods >= 3.5.0
Requires:         R-CRAN-phangorn >= 2.5.5
Requires:         R-CRAN-vcfR >= 1.8.0
Requires:         R-CRAN-future.apply >= 1.3.0
Requires:         R-CRAN-future >= 1.15.1

%description
Standardize the pre-processing of genomic variants before performing a
bacterial genome-wide association study (bGWAS). prewas creates a variant
matrix (where each row is a variant, each column is a sample, and the
entries are presence - 1 - or absence - 0 - of the variant) that can be
used as input for bGWAS tools. When creating the binary variant matrix,
prewas can perform 3 pre-processing steps including: dealing with
multiallelic SNPs, (optional) dealing with SNPs in overlapping genes, and
choosing a reference allele. prewas can output matrices for use with both
SNP-based bGWAS and gene-based bGWAS. This method is described in Saund et
al. (2019) <doi:10.1101/2019.12.20.873158>. prewas can also provide gene
matrices for variants with specific SnpEff annotations (Cingolani et al.
2012).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
