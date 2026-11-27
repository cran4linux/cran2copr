%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  prozor
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Minimal Protein Set Explaining Peptide Spectrum Matches

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-AhoCorasickTrie 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-AhoCorasickTrie 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-R6 
Requires:         R-stats 
Requires:         R-utils 

%description
Determine the minimal set of proteins that explains the peptide spectrum
matches (PSMs) of a mass spectrometry experiment, using a greedy parsimony
algorithm. Annotate peptides with the proteins they match in 'FASTA'
sequence databases, and create 'FASTA' databases with reversed decoy
sequences and contaminant proteins. Compute and plot the coverage of
protein sequences by the matched peptides. Estimate the false discovery
rate (FDR) of target-decoy search results at the PSM, precursor, peptide
and protein level, following Elias and Gygi (2007) <doi:10.1038/nmeth1019>
and Käll et al. (2008) <doi:10.1021/pr700600n>. Compute variable precursor
isolation windows for data-independent acquisition (DIA) from the
distribution of precursor (MS1) masses.

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
