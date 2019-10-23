%global packname  CollapsABEL
%global packver   0.10.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.11
Release:          1%{?dist}
Summary:          Generalized CDH (GCDH) Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
Requires:         mariadb-server
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 0.9.6
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-biganalytics 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-collUtils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-haplo.stats 
Requires:         R-CRAN-rJava >= 0.9.6
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-biganalytics 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-collUtils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-haplo.stats 

%description
Implements a generalized version of the CDH test
(<DOI:10.1371/journal.pone.0028145> and <DOI:10.1186/s12859-016-1006-9>)
for detecting compound heterozygosity on a genome-wide level, due to usage
of generalized linear models it allows flexible analysis of binary and
continuous traits with covariates.

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
%{rlibdir}/%{packname}/INDEX
