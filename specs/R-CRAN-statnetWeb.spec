%global packname  statnetWeb
%global packver   0.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          2%{?dist}
Summary:          A Graphical User Interface for Network Modeling with 'Statnet'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ergm >= 3.10.4
BuildRequires:    R-CRAN-shiny >= 1.3
BuildRequires:    R-CRAN-network 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-ergm >= 3.10.4
Requires:         R-CRAN-shiny >= 1.3
Requires:         R-CRAN-network 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-RColorBrewer 

%description
A graphical user interface for network modeling with the 'statnet'
software <https://github.com/statnet>.

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
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
