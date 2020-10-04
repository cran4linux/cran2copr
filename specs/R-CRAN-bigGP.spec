%global packname  bigGP
%global packver   0.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Distributed Gaussian Process Calculations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    openmpi-devel
Requires:         openmpi
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rmpi >= 0.6.2
BuildRequires:    R-methods 
Requires:         R-CRAN-Rmpi >= 0.6.2
Requires:         R-methods 

%description
Distributes Gaussian process calculations across nodes in a distributed
memory setting, using Rmpi. The bigGP class provides high-level methods
for maximum likelihood with normal data, prediction, calculation of
uncertainty (i.e., posterior covariance calculations), and simulation of
realizations. In addition, bigGP provides an API for basic matrix
calculations with distributed covariance matrices, including Cholesky
decomposition, back/forwardsolve, crossproduct, and matrix multiplication.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
