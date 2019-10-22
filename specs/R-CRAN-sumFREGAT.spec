%global packname  sumFREGAT
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Fast Region-Based Association Tests on Summary Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-seqminer 
BuildRequires:    R-CRAN-GBJ 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-splines 
Requires:         R-CRAN-seqminer 
Requires:         R-CRAN-GBJ 

%description
An adaptation of classical region/gene-based association analysis
techniques to the use of summary statistics (P values and effect sizes)
and correlations between genetic variants as input. It is a tool to
perform the most popular and efficient gene-based tests using the results
of genome-wide association (meta-)analyses without having the original
genotypes and phenotypes at hand.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/testfiles
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
