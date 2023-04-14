%global __brp_check_rpaths %{nil}
%global packname  Cluster.OBeu
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          3%{?dist}%{?buildtag}
Summary:          Cluster Analysis 'OpenBudgets.eu'

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-clValid 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-car 
Requires:         R-cluster 
Requires:         R-CRAN-clValid 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-dendextend 
Requires:         R-graphics 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-mclust 
Requires:         R-methods 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Estimate and return the needed parameters for visualisations designed for
'OpenBudgets' <http://openbudgets.eu/> data. Calculate cluster analysis
measures in Budget data of municipalities across Europe, according to the
'OpenBudgets' data model. It involves a set of techniques and algorithms
used to find and divide the data into groups of similar observations.
Also, can be used generally to extract visualisation parameters convert
them to 'JSON' format and use them as input in a different graphical
interface.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
