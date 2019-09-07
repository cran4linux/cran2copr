%global packname  whiboclustering
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          White Box Clustering Algorithm Design

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-clusterCrit 
BuildRequires:    R-cluster 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-clusterCrit 
Requires:         R-cluster 

%description
White Box Cluster Algorithm Design allows you to create Representative
based cluster algorithm by using reusable components. This way one can
recreate already available cluster algorithms (i.e. K-Means, K-Means++,
PAM) but also create new cluster algorithms not available in the
literature or any other software. For more information see papers
<doi:10.1007/s10462-009-9133-6> and <doi:10.1016/j.datak.2012.03.005>.

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
