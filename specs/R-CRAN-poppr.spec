%global packname  poppr
%global packver   2.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.3
Release:          1%{?dist}
Summary:          Genetic Analysis of Populations with Mixed Reproduction

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-CRAN-ape >= 3.1.1
BuildRequires:    R-CRAN-adegenet >= 2.0.0
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.4
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-pegas 
BuildRequires:    R-CRAN-polysat 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-ape >= 3.1.1
Requires:         R-CRAN-adegenet >= 2.0.0
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.4
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-phangorn 
Requires:         R-methods 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-pegas 
Requires:         R-CRAN-polysat 
Requires:         R-CRAN-rlang 
Requires:         R-boot 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-magrittr 

%description
Population genetic analyses for hierarchical analysis of partially clonal
populations built upon the architecture of the 'adegenet' package.
Originally described in Kamvar, Tabima, and Grünwald (2014)
<doi:10.7717/peerj.281> with version 2.0 described in Kamvar, Brooks, and
Grünwald (2015) <doi:10.3389/fgene.2015.00208>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/files
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
