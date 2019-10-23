%global packname  RSNNS
%global packver   0.4-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.12
Release:          1%{?dist}
Summary:          Neural Networks using the Stuttgart Neural Network Simulator(SNNS)

License:          LGPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-Rcpp >= 0.8.5
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.8.5
Requires:         R-methods 

%description
The Stuttgart Neural Network Simulator (SNNS) is a library containing many
standard implementations of neural networks. This package wraps the SNNS
functionality to make it available from within R. Using the 'RSNNS'
low-level interface, all of the algorithmic functionality and flexibility
of SNNS can be accessed. Furthermore, the package contains a convenient
high-level interface, so that the most common neural network topologies
and learning algorithms integrate seamlessly into R.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
