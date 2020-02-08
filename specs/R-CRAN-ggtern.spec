%global packname  ggtern
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}
Summary:          An Extension to 'ggplot2', for the Creation of Ternary Diagrams

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-compositions >= 1.40.2
BuildRequires:    R-CRAN-latex2exp >= 0.4
BuildRequires:    R-CRAN-scales >= 0.3.0
BuildRequires:    R-CRAN-gtable >= 0.1.2
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-proto 
BuildRequires:    R-utils 
BuildRequires:    R-lattice 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-compositions >= 1.40.2
Requires:         R-CRAN-latex2exp >= 0.4
Requires:         R-CRAN-scales >= 0.3.0
Requires:         R-CRAN-gtable >= 0.1.2
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-proto 
Requires:         R-utils 
Requires:         R-lattice 

%description
Extends the functionality of 'ggplot2', providing the capability to plot
ternary diagrams for (subset of) the 'ggplot2' geometries. Additionally,
'ggtern' has implemented several NEW geometries which are unavailable to
the standard 'ggplot2' release. For further examples and documentation,
please proceed to the 'ggtern' website.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/staticdocs
%{rlibdir}/%{packname}/INDEX
