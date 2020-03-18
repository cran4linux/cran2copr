%global packname  DoE.base
%global packver   1.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Full Factorials, Orthogonal Arrays and Base Utilities for DoEPackages

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-conf.design 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-MASS 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-partitions 
Requires:         R-grid 
Requires:         R-CRAN-conf.design 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-combinat 
Requires:         R-MASS 
Requires:         R-lattice 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-partitions 

%description
Creates full factorial experimental designs and designs based on
orthogonal arrays for (industrial) experiments. Provides diverse quality
criteria. Provides utility functions for the class design, which is also
used by other packages for designed experiments.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
