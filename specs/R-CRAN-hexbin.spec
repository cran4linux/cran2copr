%global packname  hexbin
%global packver   1.28.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.28.0
Release:          1%{?dist}
Summary:          Hexagonal Binning Routines

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.1
Requires:         R-core >= 2.0.1
BuildRequires:    R-methods 
BuildRequires:    R-lattice 
BuildRequires:    R-grid 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-lattice 
Requires:         R-grid 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Binning and plotting functions for hexagonal bins.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
