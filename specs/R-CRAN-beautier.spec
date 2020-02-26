%global packname  beautier
%global packver   2.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.5
Release:          1%{?dist}
Summary:          'BEAUti' from R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-assertive 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-testit 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-assertive 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-testit 

%description
'BEAST2' (<https://www.beast2.org>) is a widely used Bayesian phylogenetic
tool, that uses DNA/RNA/protein data and many model priors to create a
posterior of jointly estimated phylogenies and parameters. 'BEAUti 2'
(which is part of 'BEAST2') is a GUI tool that allows users to specify the
many possible setups and generates the XML file 'BEAST2' needs to run.
This package provides a way to create 'BEAST2' input files without active
user input, but using R function calls instead.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
