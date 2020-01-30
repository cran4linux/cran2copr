%global packname  icesTAF
%global packver   3.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.3
Release:          1%{?dist}
Summary:          Functions to Support the ICES Transparent Assessment Framework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-bibtex 
Requires:         R-grDevices 
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-bibtex 

%description
Functions to support the ICES Transparent Assessment Framework
<https://taf.ices.dk> to organize data, methods, and results used in ICES
assessments. ICES is an organization facilitating international
collaboration in marine science.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
