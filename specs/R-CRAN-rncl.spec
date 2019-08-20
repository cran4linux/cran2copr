%global packname  rncl
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}
Summary:          An Interface to the Nexus Class Library

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-CRAN-progress >= 1.1.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-stats 
Requires:         R-CRAN-progress >= 1.1.2
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-stats 

%description
An interface to the Nexus Class Library which allows parsing of NEXUS,
Newick and other phylogenetic tree file formats. It provides elements of
the file that can be used to build phylogenetic objects such as ape's
'phylo' or phylobase's 'phylo4(d)'. This functionality is demonstrated
with 'read_newick_phylo()' and 'read_nexus_phylo()'.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/newick_bad
%doc %{rlibdir}/%{packname}/newick_good
%doc %{rlibdir}/%{packname}/nexusfiles
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
