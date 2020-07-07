%global packname  RANN
%global packver   2.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.1
Release:          3%{?dist}
Summary:          Fast Nearest Neighbour Search (Wraps ANN Library) Using L2Metric

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core

%description
Finds the k nearest neighbours for every point in a given dataset in O(N
log N) time using Arya and Mount's ANN library (v1.1.3). There is support
for approximate as well as exact searches, fixed radius searches and 'bd'
as well as 'kd' trees. The distance is computed using the L2 (Euclidean)
metric. Please see package 'RANN.L1' for the same functionality using the
L1 (Manhattan, taxicab) metric.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHT
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
