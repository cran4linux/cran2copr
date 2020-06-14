%global packname  bootcluster
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Bootstrapping Estimates of Clustering Stability

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-plyr 
Requires:         R-cluster 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-sets 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-plyr 

%description
Implementation of the bootstrapping approach for the estimation of
clustering stability on observation and cluster level, as well as its
application in estimating the number of clusters.

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
