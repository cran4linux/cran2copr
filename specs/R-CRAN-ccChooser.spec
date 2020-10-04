%global packname  ccChooser
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          3%{?dist}%{?buildtag}
Summary:          Developing a core collections

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-cluster >= 1.13.1
Requires:         R-cluster >= 1.13.1

%description
ccChooser can be used to developing and evaluation of core collections for
germplasm collections (entire collection). This package used to develop a
core collection for biological resources like genbanks. A core collection
is defined as a sample of accessions that represent, with the lowest
possible level of redundancy, the genetic diversity (the richness of gene
or genotype categories) of the entire collection. The establishing a core
collection that represents genetic diversity of the entire collection with
minimum loss of its original diversity and minimum redundancies is an
important problem for gene-banks curators and crop breeders. ccChooser
establish core collection base on phenotypic data (agronomic,
morphological, phenological).

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
%{rlibdir}/%{packname}/INDEX
