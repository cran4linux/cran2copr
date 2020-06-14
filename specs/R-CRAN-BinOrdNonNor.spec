%global packname  BinOrdNonNor
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          2%{?dist}
Summary:          Concurrent Generation of Binary, Ordinal and Continuous Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GenOrd 
BuildRequires:    R-CRAN-OrdNor 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-GenOrd 
Requires:         R-CRAN-OrdNor 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-corpcor 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 

%description
Generation of samples from a mix of binary, ordinal and continuous random
variables with a pre-specified correlation matrix and marginal
distributions. The details of the method are explained in Demirtas et al.
(2012) <DOI:10.1002/sim.5362>.

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
%{rlibdir}/%{packname}/INDEX
