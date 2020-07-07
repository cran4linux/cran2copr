%global packname  rTableICC
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          3%{?dist}
Summary:          Random Generation of Contingency Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-aster 
BuildRequires:    R-stats 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-aster 
Requires:         R-stats 

%description
Contains functions for random generation of R x C and 2 x 2 x K
contingency tables. In addition to the generation of contingency tables
over predetermined intraclass-correlated clusters, it is possible to
generate contingency tables without intraclass correlations under product
multinomial, multinomial, and Poisson sampling plans. It also consists of
a function for generation of random data from a given discrete probability
distribution function. See Demirhan (2016)
<https://journal.r-project.org/archive/2016-1/demirhan.pdf> for more
information.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
