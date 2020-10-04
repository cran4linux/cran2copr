%global packname  kml3d
%global packver   2.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.2
Release:          3%{?dist}%{?buildtag}
Summary:          K-Means for Joint Longitudinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-longitudinalData >= 2.4.1
BuildRequires:    R-CRAN-kml >= 2.4.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-clv 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-misc3d 
Requires:         R-CRAN-longitudinalData >= 2.4.1
Requires:         R-CRAN-kml >= 2.4.1
Requires:         R-methods 
Requires:         R-CRAN-clv 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-misc3d 

%description
An implementation of k-means specifically design to cluster joint
trajectories (longitudinal data on several variable-trajectories). Like
'kml', it provides facilities to deal with missing value, compute several
quality criterion (Calinski and Harabatz, Ray and Turie, Davies and
Bouldin, BIC,...) and propose a graphical interface for choosing the
'best' number of clusters. In addition, the 3D graph representing the mean
joint-trajectories of each cluster can be exported through LaTeX in a 3D
dynamic rotating PDF graph.

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
%{rlibdir}/%{packname}/INDEX
