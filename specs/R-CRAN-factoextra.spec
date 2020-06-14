%global packname  factoextra
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          2%{?dist}
Summary:          Extract and Visualize the Results of Multivariate Data Analyses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-ggpubr >= 0.1.5
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-ggpubr >= 0.1.5
Requires:         R-CRAN-abind 
Requires:         R-cluster 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-FactoMineR 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-tidyr 

%description
Provides some easy-to-use functions to extract and visualize the output of
multivariate data analyses, including 'PCA' (Principal Component
Analysis), 'CA' (Correspondence Analysis), 'MCA' (Multiple Correspondence
Analysis), 'FAMD' (Factor Analysis of Mixed Data), 'MFA' (Multiple Factor
Analysis) and 'HMFA' (Hierarchical Multiple Factor Analysis) functions
from different R packages. It contains also functions for simplifying some
clustering analysis steps and provides 'ggplot2' - based elegant data
visualization.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
