%global packname  AssocAFC
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Allele Frequency Comparison

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CompQuadForm 
Requires:         R-CRAN-CompQuadForm 

%description
When doing association analysis one does not always have the genotypes for
the control population.  In such cases it may be necessary to fall back on
frequency based tests using well known sources for the frequencies in the
control population, for instance, from the 1000 Genomes Project.  The
Allele Frequency Comparison ('AssocAFC') package performs multiple rare
variant association analyses in both population and family-based GWAS
(Genome-Wide Association Study) designs. It includes three score tests
that are based on the difference of the sum of allele frequencies between
cases and controls.  Two of these tests, Wcorrected() and Wqls(), are
collapsing-based tests and suffer from having protective and risk
variants. The third test, afcSKAT(), is a score test that overcomes the
mix of SNP (Single-Nucleotide Polymorphism) effect directions. For more
details see Saad M and Wijsman EM (2017) <doi:10.1093/bib/bbx107>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
