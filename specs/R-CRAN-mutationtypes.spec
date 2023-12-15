%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mutationtypes
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Validate and Convert Mutational Impacts Using Standard Genomic Dictionaries

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-assertions 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-assertions 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-stats 
Requires:         R-utils 

%description
Check concordance of a vector of mutation impacts with standard
dictionaries such as Sequence Ontology (SO)
<http://www.sequenceontology.org/>, Mutation Annotation Format (MAF)
<https://docs.gdc.cancer.gov/Encyclopedia/pages/Mutation_Annotation_Format_TCGAv2/>
or Prediction and Annotation of Variant Effects (PAVE)
<https://github.com/hartwigmedical/hmftools/tree/master/pave>. It enables
conversion between SO/PAVE and MAF terms and selection of the most severe
consequence where multiple ampersand (&) delimited impacts are given.

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
