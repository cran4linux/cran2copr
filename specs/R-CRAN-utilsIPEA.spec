%global packname  utilsIPEA
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          3%{?dist}
Summary:          IPEA Common Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-dplyr 

%description
The most used functions on IPEA (Instituto de Pesquisa Economica
Aplicada). Most of functions deal with brazilian names. It can guess the
women single's name, extract prepositions or extract the first name.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
