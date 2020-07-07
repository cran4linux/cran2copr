%global packname  inaparc
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Initialization Algorithms for Partitioning Cluster Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-kpeaks 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-kpeaks 
Requires:         R-CRAN-lhs 
Requires:         R-stats 
Requires:         R-methods 

%description
Partitioning clustering algorithms divide data sets into k subsets or
partitions so-called clusters. They require some initialization procedures
for starting the algorithms. Initialization of cluster prototypes is one
of such kind of procedures for most of the partitioning algorithms.
Cluster prototypes are the centers of clusters, i.e. centroids or medoids,
representing the clusters in a data set. In order to initialize cluster
prototypes, the package 'inaparc' contains a set of the functions that are
the implementations of several linear time-complexity and loglinear
time-complexity methods in addition to some novel techniques.
Initialization of fuzzy membership degrees matrices is another important
task for starting the probabilistic and possibilistic partitioning
algorithms. In order to initialize membership degrees matrices required by
these algorithms, a number of functions based on some traditional and
novel initialization techniques are also available in the package
'inaparc'.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
