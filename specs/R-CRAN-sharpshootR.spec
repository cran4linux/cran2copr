%global packname  sharpshootR
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}
Summary:          A Soil Survey Toolkit

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-aqp 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-soilDB 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-cluster 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-curl 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-aqp 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-soilDB 
Requires:         R-CRAN-igraph 
Requires:         R-cluster 
Requires:         R-lattice 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-stringi 
Requires:         R-parallel 
Requires:         R-CRAN-curl 

%description
Miscellaneous soil data management, summary, visualization, and conversion
utilities to support soil survey.

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
%{rlibdir}/%{packname}/INDEX
