%global packname  PoisBinOrd
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          2%{?dist}
Summary:          Data Generation with Poisson, Binary and Ordinal Components

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-GenOrd 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-GenOrd 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 

%description
Generation of multiple count, binary and ordinal variables simultaneously
given the marginal characteristics and association structure. Throughout
the package, the word 'Poisson' is used to imply count data under the
assumption of Poisson distribution. The details of the method are
explained in Amatya, A. and Demirtas, H. (2015)
<DOI:10.1080/00949655.2014.953534>.

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
