%global packname  rphast
%global packver   1.6.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.9
Release:          1%{?dist}
Summary:          Interface to 'PHAST' Software for Comparative Genomics

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-methods 

%description
Provides an R interface to the 'PHAST'(<http://compgen.cshl.edu/phast/>)
software (Phylogenetic Analysis with Space/Time Models).  It can be used
for many types of analysis in comparative and evolutionary genomics, such
as estimating models of evolution from sequence data, scoring alignments
for conservation or acceleration, and predicting elements based on
conservation or custom phylogenetic hidden Markov models.  It can also
perform many basic operations on multiple sequence alignments and
phylogenetic trees.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
