%global packname  genetics
%global packver   1.3.8.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.8.1.2
Release:          1%{?dist}
Summary:          Population Genetics

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-gtools 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 

%description
Classes and methods for handling genetic data. Includes classes to
represent genotypes and haplotypes at single markers up to multiple
markers on multiple chromosomes. Function include allele frequencies,
flagging homo/heterozygotes, flagging carriers of certain alleles,
estimating and testing for Hardy-Weinberg disequilibrium, estimating and
testing for linkage disequilibrium, ...

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
