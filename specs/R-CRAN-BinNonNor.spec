%global packname  BinNonNor
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          3%{?dist}
Summary:          Data Generation with Binary and Continuous Non-Normal Components

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-mvtnorm 
Requires:         R-Matrix 

%description
Generation of multiple binary and continuous non-normal variables
simultaneously given the marginal characteristics and association
structure based on the methodology proposed by Demirtas et al. (2012)
<DOI:10.1002/sim.5362>.

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
