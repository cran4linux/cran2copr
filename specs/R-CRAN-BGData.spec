%global packname  BGData
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          2%{?dist}
Summary:          A Suite of Packages for Analysis of Big Genomic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-crochet >= 2.1.0
BuildRequires:    R-CRAN-symDMatrix >= 2.0.0
BuildRequires:    R-CRAN-BEDMatrix >= 1.4.0
BuildRequires:    R-CRAN-LinkedMatrix >= 1.3.0
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-synchronicity 
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-CRAN-bit 
Requires:         R-CRAN-crochet >= 2.1.0
Requires:         R-CRAN-symDMatrix >= 2.0.0
Requires:         R-CRAN-BEDMatrix >= 1.4.0
Requires:         R-CRAN-LinkedMatrix >= 1.3.0
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-synchronicity 
Requires:         R-CRAN-ff 
Requires:         R-CRAN-bit 

%description
An umbrella package providing a phenotype/genotype data structure and
scalable and efficient computational methods for large genomic datasets in
combination with several other packages: 'BEDMatrix', 'LinkedMatrix', and
'symDMatrix'.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
