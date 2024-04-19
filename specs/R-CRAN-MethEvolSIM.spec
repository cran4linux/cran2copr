%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MethEvolSIM
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate DNA Methylation Dynamics on Different Genomic Structures along Genealogies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-R6 

%description
DNA methylation is an epigenetic modification involved in genomic
stability, gene regulation, development and disease. DNA methylation
occurs mainly through the addition of a methyl group to cytosines, for
example to cytosines in a CpG dinucleotide context (CpG stands for a
cytosine followed by a guanine). Tissue-specific methylation patterns lead
to genomic regions with different characteristic methylation levels. E.g.
in vertebrates CpG islands (regions with high CpG content) that are
associated to promoter regions of expressed genes tend to be unmethylated.
'MethEvolSIM' is a model-based simulation software for the generation and
modification of cytosine methylation patterns along a given tree, which
can be a genealogy of cells within an organism, a coalescent tree of DNA
sequences sampled from a population, or a species tree. The simulations
are based on an extension of the model of Grosser & Metzler (2020)
<doi:10.1186/s12859-020-3438-5> and allows for changes of the methylation
states at single cytosine positions as well as simultaneous changes of
methylation frequencies in genomic structures like CpG islands.

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
