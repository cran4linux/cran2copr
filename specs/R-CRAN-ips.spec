%global packname  ips
%global packver   0.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.11
Release:          1%{?dist}
Summary:          Interfaces to Phylogenetic Software in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-XML 

%description
Functions that wrap popular phylogenetic software for sequence alignment,
masking of sequence alignments, and estimation of phylogenies and
ancestral character states.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
