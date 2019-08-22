%global packname  sapa
%global packver   2.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Spectral Analysis for Physical Applications

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-ifultools >= 2.0.0
BuildRequires:    R-CRAN-splus2R >= 1.2.0
BuildRequires:    R-methods 
Requires:         R-CRAN-ifultools >= 2.0.0
Requires:         R-CRAN-splus2R >= 1.2.0
Requires:         R-methods 

%description
Software for the book Spectral Analysis for Physical Applications, Donald
B. Percival and Andrew T. Walden, Cambridge University Press, 1993.

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
%doc %{rlibdir}/%{packname}/sapa.chm
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
