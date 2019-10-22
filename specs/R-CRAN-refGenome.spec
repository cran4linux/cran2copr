%global packname  refGenome
%global packver   1.7.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.7
Release:          1%{?dist}
Summary:          Gene and Splice Site Annotation Using Annotation Data from'Ensembl' and 'UCSC' Genome Browsers

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-DBI 
Requires:         R-methods 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-DBI 

%description
Contains functionalities for importing and managing downloaded genome
annotation data from 'Ensembl' genome browser (European Bioinformatics
Institute, <https://www.ensembl.org>) and from 'UCSC' genome browser
(University of California, Santa Cruz, <https://genome.ucsc.edu/>) and
annotation routines for genomic positions and splice site positions.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
