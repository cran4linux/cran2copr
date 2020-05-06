%global packname  dispRity
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Measuring Disparity

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-castor 
BuildRequires:    R-CRAN-Claddis 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-geoscale 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-phyclust 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ape 
Requires:         R-stats 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-castor 
Requires:         R-CRAN-Claddis 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-geoscale 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-phyclust 
Requires:         R-utils 
Requires:         R-CRAN-vegan 

%description
A modular package for measuring disparity (multidimensional space
occupancy). Disparity can be calculated from any matrix defining a
multidimensional space. The package provides a set of implemented metrics
to measure properties of the space and allows users to provide and test
their own metrics (Guillerme (2018) <doi:10.1111/2041-210X.13022>). The
package also provides functions for looking at disparity in a serial way
(e.g. disparity through time - Guillerme and Cooper (2018)
<doi:10.1111/pala.12364>) or per groups as well as visualising the
results. Finally, this package provides several statistical tests for
disparity analysis.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/packages.bib
%doc %{rlibdir}/%{packname}/References.bib
%doc %{rlibdir}/%{packname}/vignettes
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
