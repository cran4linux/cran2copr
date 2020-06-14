%global packname  ecespa
%global packver   1.1-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.11
Release:          2%{?dist}
Summary:          Functions for Spatial Point Pattern Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-spatstat 
Requires:         R-CRAN-spatstat 

%description
Some wrappers, functions and data sets for for spatial point pattern
analysis (mainly based on 'spatstat'), used in the book "Introduccion al
Analisis Espacial de Datos en Ecologia y Ciencias Ambientales: Metodos y
Aplicaciones" and in the papers by De la Cruz et al. (2008)
<doi:10.1111/j.0906-7590.2008.05299.x> and Olano et al. (2009)
<doi:10.1051/forest:2008074>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
