%global packname  SmallCountRounding
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          2%{?dist}
Summary:          Small Count Rounding of Tabular Data

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-SSBtools 
BuildRequires:    R-methods 
Requires:         R-Matrix 
Requires:         R-CRAN-SSBtools 
Requires:         R-methods 

%description
A statistical disclosure control tool to protect frequency tables in cases
where small values are sensitive. The function PLSrounding() performs
small count rounding of necessary inner cells so that all small
frequencies of cross-classifications to be published (publishable cells)
are rounded. This is equivalent to changing micro data since frequencies
of unique combinations are changed. Thus, additivity and consistency are
guaranteed. The methodology is described in Langsrud and Heldal (2018)
<https://www.researchgate.net/publication/327768398>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
