%global packname  RcmdrPlugin.EACSPIR
%global packver   0.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          2%{?dist}
Summary:          Plugin de R-Commander para el Manual 'EACSPIR'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.1.6
BuildRequires:    R-CRAN-R2HTML 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-ez 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-RcmdrMisc 
Requires:         R-CRAN-Rcmdr >= 2.1.6
Requires:         R-CRAN-R2HTML 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-ez 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-RcmdrMisc 

%description
Este paquete proporciona una interfaz grafica de usuario (GUI) para
algunos de los procedimientos estadisticos detallados en un curso de
'Estadistica aplicada a las Ciencias Sociales mediante el programa
informatico R' (EACSPIR). LA GUI se ha desarrollado como un Plugin del
programa R-Commander.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/INDEX
