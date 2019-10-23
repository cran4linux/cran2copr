%global packname  FlowCAr
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Flow Network Construction and Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-LIM 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-enaR 
Requires:         R-CRAN-LIM 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-enaR 

%description
Creates and assesses a list of possible networks solved using 'LIM'
(Linear Inverse Modelling) (Soetaert, Karline, and Dick Van Oevelen (2009)
<doi:10.1007/s10021-009-9297-6>) and restructuring this list, enabling ENA
(Ecological Network Analysis) to be performed on the flow network in R
package 'enaR' (Borrett, Stuart R., and Matthew K. Lau (2014)
<doi:10.1111/2041-210X.12282>).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
