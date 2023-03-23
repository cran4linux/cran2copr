%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MHCtools
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
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
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-openxlsx 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-mgcv 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-openxlsx 

%description
Fifteen tools for bioinformatics processing and analysis of major
histocompatibility complex (MHC) data. The functions are tailored for
amplicon data sets that have been filtered using the dada2 method (for
more information on dada2, visit <https://benjjneb.github.io/dada2/> ),
but even other types of data sets can be analyzed. The ReplMatch()
function matches replicates in data sets in order to evaluate genotyping
success. The GetReplTable() and GetReplStats() functions perform such an
evaluation. The CreateFas() function creates a fasta file with all the
sequences in the data set. The CreateSamplesFas() function creates
individual fasta files for each sample in the data set. The DistCalc()
function calculates Grantham, Sandberg, or p-distances from pairwise
comparisons of all sequences in a data set, and mean distances of all
pairwise comparisons within each sample in a data set. The function
additionally outputs five tables with physico-chemical z-descriptor values
(based on Sandberg et al. 1998) for each amino acid position in all
sequences in the data set. These tables may be useful for further
downstream analyses, such as estimation of MHC supertypes. The
BootKmeans() function is a wrapper for the kmeans() function of the
'stats' package, which allows for bootstrapping. Bootstrapping k-estimates
may be desirable in data sets, where e.g. BIC- vs. k-values do not produce
clear inflection points ("elbows"). BootKmeans() performs multiple runs of
kmeans() and estimates optimal k-values based on a user-defined threshold
of BIC reduction. The method is an automated and bootstrapped version of
visually inspecting elbow plots of BIC- vs. k-values. The ClusterMatch()
function is a tool for evaluating whether different k-means() clustering
models identify similar clusters, and summarize bootstrap model stats as
means for different estimated values of k. It is designed to take files
produced by the BootKmeans() function as input, but other data can be
analysed if the descriptions of the required data formats are observed
carefully. The PapaDiv() function compares parent pairs in the data set
and calculate their joint MHC diversity, taking into account sequence
variants that occur in both parents. The HpltFind() function infers
putative haplotypes from families in the data set. The GetHpltTable() and
GetHpltStats() functions evaluate the accuracy of the haplotype inference.
The CreateHpltOccTable() function creates a binary (logical)
haplotype-sequence occurrence matrix from the output of HpltFind(), for
easy overview of which sequences are present in which haplotypes. The
HpltMatch() function compares haplotypes to help identify overlapping and
potentially identical types. The NestTablesXL() function translates the
output from HpltFind() to an Excel workbook, that provides a convenient
overview for evaluation and curating of the inferred putative haplotypes.

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
