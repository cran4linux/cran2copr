%global packname  JuniperKernel
%global packver   1.4.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1.0
Release:          1%{?dist}
Summary:          Kernel for 'Jupyter'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    zeromq-devel
Requires:         zeromq
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-pbdZMQ >= 0.3.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-gdtools >= 0.1.6
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-repr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
Requires:         R-CRAN-pbdZMQ >= 0.3.2
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-gdtools >= 0.1.6
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-repr 
Requires:         R-CRAN-data.table 
Requires:         R-methods 

%description
Provides a full implementation of the 'Jupyter' <http://jupyter.org/>
messaging protocol in C++ by leveraging 'Rcpp' and 'Xeus'
<https://github.com/QuantStack/xeus>. 'Jupyter' supplies an interactive
computing environment and a messaging protocol defined over 'ZeroMQ' for
multiple programming languages. This package implements the 'Jupyter'
kernel interface so that 'R' is exposed to this interactive computing
environment. 'ZeroMQ' functionality is provided by the 'pbdZMQ' package.
'Xeus' is a C++ library that facilitates the implementation of kernels for
'Jupyter'. Additionally, 'Xeus' provides an interface to libraries that
exist in the 'Jupyter' ecosystem for building widgets, plotting, and more
<https://blog.jupyter.org/interactive-workflows-for-c-with-jupyter-fe9b54227d92>.
'JuniperKernel' uses 'Xeus' as a library for the 'Jupyter' messaging
protocol.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/runits
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
