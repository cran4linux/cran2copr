%global packname  polysat
%global packver   1.7-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.4
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Polyploid Microsatellite Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 

%description
A collection of tools to handle microsatellite data of any ploidy (and
samples of mixed ploidy) where allele copy number is not known in
partially heterozygous genotypes.  It can import and export data in ABI
'GeneMapper', 'Structure', 'ATetra', 'Tetrasat'/'Tetra', 'GenoDive',
'SPAGeDi', 'POPDIST', 'STRand', and binary presence/absence formats.  It
can calculate pairwise distances between individuals using a stepwise
mutation model or infinite alleles model, with or without taking ploidies
and allele frequencies into account.  These distances can be used for the
calculation of clonal diversity statistics or used for further analysis in
R.  Allelic diversity statistics and Polymorphic Information Content are
also available.  polysat can assist the user in estimating the ploidy of
samples, and it can estimate allele frequencies in populations, calculate
pairwise or global differentiation statistics based on those frequencies,
and export allele frequencies to 'SPAGeDi' and 'adegenet'. Functions are
also included for assigning alleles to isoloci in cases where one pair of
microsatellite primers amplifies alleles from two or more independently
segregating isoloci.  polysat is described by Clark and Jasieniuk (2011)
<doi:10.1111/j.1755-0998.2011.02985.x> and Clark and Schreier (2017)
<doi:10.1111/1755-0998.12639>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
