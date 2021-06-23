%global __brp_check_rpaths %{nil}
%global packname  ftrCOOL
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Extraction from Biological Sequences

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Extracts features from biological sequences. It contains most features
which are presented in related work and also includes features which have
never been introduced before. It extracts numerous features from
nucleotide and peptide sequences. Each feature converts the input
sequences to discrete numbers in order to use them as predictors in
machine learning models. There are many features and information which are
hidden inside a sequence. Utilizing the package, users can convert
biological sequences to discrete models based on chosen properties.
References: 'iLearn' 'Z. Chen et al.' (2019) <DOI:10.1093/bib/bbz041>.
'iFeature' 'Z. Chen et al.' (2018) <DOI:10.1093/bioinformatics/bty140>.
<https://CRAN.R-project.org/package=rDNAse>. 'PseKRAAC' 'Y. Zuo et al.'
'PseKRAAC: a flexible web server for generating pseudo K-tuple reduced
amino acids composition' (2017) <DOI:10.1093/bioinformatics/btw564>.
'iDNA6mA-PseKNC' 'P. Feng et al.' 'iDNA6mA-PseKNC: Identifying DNA
N6-methyladenosine sites by incorporating nucleotide physicochemical
properties into PseKNC' (2019) <DOI:10.1016/j.ygeno.2018.01.005>. 'I.
Dubchak et al.' 'Prediction of protein folding class using global
description of amino acid sequence' (1995) <DOI:10.1073/pnas.92.19.8700>.
'W. Chen et al.' 'Identification and analysis of the N6-methyladenosine in
the Saccharomyces cerevisiae transcriptome' (2015)
<DOI:10.1038/srep13859>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
