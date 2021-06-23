%global __brp_check_rpaths %{nil}
%global packname  MHCtools
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of MHC Data in Non-Model Species

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Ten tools for bioinformatical processing and analysis of major
histocompatibility complex (MHC) data. The functions are tailored for
amplicon data sets that have been filtered using the 'dada2' method (for
more information on 'dada2', visit <https://benjjneb.github.io/dada2/> ),
but even other types of data sets can be analyzed. The DistCalc() function
calculates Grantham, Sandberg, or p-distances from pairwise comparisons of
all sequences in a data set, and mean distances of all pairwise
comparisons within each sample in a data set. The function additionally
outputs five tables with physico-chemical z-descriptor values (based on
Sandberg et al. 1998) for each amino acid position in all sequences in the
data set. These tables may be useful for further downstream analyses, such
as estimation of MHC supertypes. The HpltFind() function infers putative
haplotypes from families in the data set. The GetHpltTable() and
GetHpltStats() functions evaluate the accuracy of the haplotype inference.
The PapaDiv() function compares parent pairs in the data set and calculate
their joint MHC diversity, taking into account sequence variants that
occur in both parents. The ReplMatch() function matches replicates in data
sets in order to evaluate genotyping success. The GetReplTable() and
GetReplStats() functions perform such an evaluation. The CreateFas()
function creates a fasta file with all the sequences in the data set. The
CreateSamplesFas() function creates individual fasta files for each sample
in the data set.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
