%global packname  ChaosGame
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          2%{?dist}
Summary:          Chaos Game

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-sphereplot 
BuildRequires:    R-CRAN-plot3D 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-sphereplot 
Requires:         R-CRAN-plot3D 

%description
The main objective of the package is to enter a word of at least two
letters based on which an Iterated Function System with Probabilities is
constructed, and a two-dimensional fractal containing the chosen word
infinitely often is generated via the Chaos Game. Additionally, the
package allows to project the two-dimensional fractal on several
three-dimensional surfaces and to transform the fractal into another
fractal with uniform marginals.

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
%{rlibdir}/%{packname}/INDEX
