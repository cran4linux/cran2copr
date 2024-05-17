%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ClusTCR2
%global packver   1.7.3.01
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.3.01
Release:          1%{?dist}%{?buildtag}
Summary:          Identifying Similar T Cell Receptor Hyper-Variable Sequences with 'ClusTCR2'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggseqlogo 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-VLF 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggseqlogo 
Requires:         R-CRAN-network 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-VLF 

%description
Enhancing T cell receptor (TCR) sequence analysis, 'ClusTCR2', based on
'ClusTCR' python program, leverages Hamming distance to compare the
complement-determining region three (CDR3) sequences for sequence
similarity, variable gene (V gene) and length. The second step employs the
Markov Cluster Algorithm to identify clusters within an undirected graph,
providing a summary of amino acid motifs and matrix for generating network
plots. Tailored for single-cell RNA-seq data with integrated TCR-seq
information, 'ClusTCR2' is integrated into the Single Cell TCR and
Expression Grouped Ontologies (STEGO) R application or 'STEGO.R'. See the
two publications for more details. Sebastiaan Valkiers, Max Van Houcke,
Kris Laukens, Pieter Meysman (2021) <doi:10.1093/bioinformatics/btab446>,
Kerry A. Mullan, My Ha, Sebastiaan Valkiers, Nicky de Vrij, Benson
Ogunjimi, Kris Laukens, Pieter Meysman (2023)
<doi:10.1101/2023.09.27.559702>.

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
