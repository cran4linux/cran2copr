%global packname  PoisBinOrdNonNor
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          2%{?dist}
Summary:          Generation of Up to Four Different Types of Variables

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-GenOrd 
BuildRequires:    R-CRAN-BB 
Requires:         R-Matrix 
Requires:         R-CRAN-corpcor 
Requires:         R-MASS 
Requires:         R-CRAN-GenOrd 
Requires:         R-CRAN-BB 

%description
Generation of a chosen number of count, binary, ordinal, and continuous
random variables, with specified correlations and marginal properties. The
details of the method are explained in Demirtas (2012)
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
