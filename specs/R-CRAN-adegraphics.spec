%global __brp_check_rpaths %{nil}
%global packname  adegraphics
%global packver   1.0-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.15
Release:          3%{?dist}%{?buildtag}
Summary:          An S4 Lattice-Based Package for the Representation ofMultivariate Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ade4 >= 1.7.13
BuildRequires:    R-CRAN-sp >= 1.1.1
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
Requires:         R-CRAN-ade4 >= 1.7.13
Requires:         R-CRAN-sp >= 1.1.1
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-KernSmooth 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 

%description
Graphical functionalities for the representation of multivariate data. It
is a complete re-implementation of the functions available in the 'ade4'
package.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
