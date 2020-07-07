%global packname  riceidconverter
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Convert Biological ID from RAP or MSU to SYMBOL for Oryza Sativa

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-dplyr 

%description
Convert one biological ID to another of rice (Oryza sativa). Rice(Oryza
sativa) has more than one form gene ID for the genome. The two main gene
ID for rice genome are the RAP (The Rice Annotation Project,
<https://rapdb.dna.affrc.go.jp/>, and the MSU(The Rice Genome Annotation
Project, <http://rice.plantbiology.msu.edu/>. All RAP rice gene IDs are of
the form Os##g####### as explained on the website
<https://rapdb.dna.affrc.go.jp/>. All MSU rice gene IDs are of the form
LOC_Os##g##### as explained on the website
<http://rice.plantbiology.msu.edu/analyses_nomenclature.shtml>. All SYMBOL
rice gene IDs are the unique name on the NCBI(National Center for
Biotechnology Information, <https://www.ncbi.nlm.nih.gov/>. The
TRANSCRIPTID, is the transcript id of rice, are of the form Os##t#######.
The researchers usually need to converter between various IDs. Such as
converter RAP to SYMBOLS for function searching on NCBI. There are a lot
of websites with the function for converting RAP to MSU or MSU to RA, such
as 'ID Converter' <https://rapdb.dna.affrc.go.jp/tools/converter>. But it
is difficult to convert super multiple IDs on these websites. The package
can convert all IDs between the three IDs (RAP, MSU and SYMBOL) regardless
of the number.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
