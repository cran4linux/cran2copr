%global packname  PAC
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Partition-Assisted Clustering and Multiple Alignments ofNetworks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.2
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-parmigene 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-Rcpp >= 0.12.2
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-parmigene 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 

%description
Implements partition-assisted clustering and multiple alignments of
networks. It 1) utilizes partition-assisted clustering to find robust and
accurate clusters and 2) discovers coherent relationships of clusters
across multiple samples. It is particularly useful for analyzing
single-cell data set. Please see Li et al. (2017)
<doi:10.1371/journal.pcbi.1005875> for detail method description.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
