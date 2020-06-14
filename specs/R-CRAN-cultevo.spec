%global packname  cultevo
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Tools, Measures and Statistical Tests for Cultural Evolution

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-pspearman 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
Requires:         R-CRAN-combinat 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-pspearman 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-utils 

%description
Provides tools for measuring the compositionality of signalling systems
(in particular the information-theoretic measure due to Spike (2016)
<http://hdl.handle.net/1842/25930> and the Mantel test for distance matrix
correlation (after Dietz 1983) <doi:10.1093/sysbio/32.1.21>), functions
for computing string and meaning distance matrices as well as an
implementation of the Page test for monotonicity of ranks (Page 1963)
<doi:10.1080/01621459.1963.10500843> with exact p-values up to k = 22.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
