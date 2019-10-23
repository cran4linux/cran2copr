%global packname  sparkTable
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          Sparklines and Graphical Tables for TeX and HTML

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-StatMatch 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-pixmap 
BuildRequires:    R-CRAN-RGraphics 
BuildRequires:    R-grid 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-Cairo 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-StatMatch 
Requires:         R-boot 
Requires:         R-CRAN-pixmap 
Requires:         R-CRAN-RGraphics 
Requires:         R-grid 

%description
Create sparklines and graphical tables for documents and websites.

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
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/shinystuff
%{rlibdir}/%{packname}/INDEX
