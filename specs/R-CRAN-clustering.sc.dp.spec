%global packname  clustering.sc.dp
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Optimal Distance-Based Clustering for Multidimensional Data withSequential Constraint

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0

%description
A dynamic programming algorithm for optimal clustering multidimensional
data with sequential constraint. The algorithm minimizes the sum of
squares of within-cluster distances. The sequential constraint allows only
subsequent items of the input data to form a cluster. The sequential
constraint is typically required in clustering data streams or items with
time stamps such as video frames, GPS signals of a vehicle, movement data
of a person, e-pen data, etc. The algorithm represents an extension of
Ckmeans.1d.dp to multiple dimensional spaces. Similarly to the
one-dimensional case, the algorithm guarantees optimality and
repeatability of clustering. Method clustering.sc.dp can find the optimal
clustering if the number of clusters is known. Otherwise, methods
findwithinss.sc.dp and backtracking.sc.dp can be used.

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
%{rlibdir}/%{packname}/libs
