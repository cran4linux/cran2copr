%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GoMiner
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Automate the Mapping Between a List of Genes and Gene Ontology Categories

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-minimalistGODB 
BuildRequires:    R-CRAN-HGNChelper 
BuildRequires:    R-CRAN-randomGODB 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vprint 
Requires:         R-CRAN-minimalistGODB 
Requires:         R-CRAN-HGNChelper 
Requires:         R-CRAN-randomGODB 
Requires:         R-stats 
Requires:         R-CRAN-gplots 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-vprint 

%description
In gene-expression microarray studies, for example, one generally obtains
a list of dozens or hundreds of genes that differ in expression between
samples and then asks 'What does all of this mean biologically?'
Alternatively, gene lists can be derived conceptually in addition to
experimentally. For instance, one might want to analyze a group of genes
known as housekeeping genes. The work of the Gene Ontology (GO) Consortium
<geneontology.org> provides a way to address that question. GO organizes
genes into hierarchical categories based on biological process, molecular
function and subcellular localization. The role of 'GoMiner' is to
automate the mapping between a list of genes and GO, and to provide a
statistical summary of the results as well as a visualization.

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
