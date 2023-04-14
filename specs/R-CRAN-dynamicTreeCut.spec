%global __brp_check_rpaths %{nil}
%global packname  dynamicTreeCut
%global packver   1.63-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.63.1
Release:          3%{?dist}%{?buildtag}
Summary:          Methods for Detection of Clusters in Hierarchical ClusteringDendrograms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.3.0
Requires:         R-core >= 2.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Contains methods for detection of clusters in hierarchical clustering
dendrograms.

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
