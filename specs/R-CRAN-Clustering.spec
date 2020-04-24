%global packname  Clustering
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}
Summary:          Execution of Multiple Clustering Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-apcluster 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-ClusterR 
BuildRequires:    R-CRAN-advclust 
BuildRequires:    R-CRAN-pvclust 
BuildRequires:    R-CRAN-gama 
BuildRequires:    R-CRAN-amap 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-apcluster 
Requires:         R-cluster 
Requires:         R-CRAN-ClusterR 
Requires:         R-CRAN-advclust 
Requires:         R-CRAN-pvclust 
Requires:         R-CRAN-gama 
Requires:         R-CRAN-amap 
Requires:         R-stats 
Requires:         R-CRAN-pracma 
Requires:         R-tools 
Requires:         R-CRAN-gmp 
Requires:         R-utils 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 

%description
The design of this package allows us to run different clustering packages
and compare the results between them, to determine which algorithm behaves
best from the data provided.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
