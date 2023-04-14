%global __brp_check_rpaths %{nil}
%global packname  Sofi
%global packver   0.16.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.4.8
Release:          3%{?dist}%{?buildtag}
Summary:          Interfaz interactiva con fines didacticos

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-foreign 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-sampling 
Requires:         R-foreign 

%description
Este paquete tiene la finalidad de ayudar a aprender de una forma
interactiva, teniendo ejemplos y la posibilidad de resolver nuevos al
mismo tiempo. Apuntes de clase interactivos.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
