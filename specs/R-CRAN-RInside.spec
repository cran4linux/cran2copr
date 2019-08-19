%global packname  RInside
%global packver   0.2.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.15
Release:          1%{?dist}
Summary:          C++ Classes to Embed R in C++ Applications

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-Rcpp >= 0.11.0

%description
C++ classes to embed R in C++ applications A C++ class providing the R
interpreter is offered by this package making it easier to have "R inside"
your C++ application. As R itself is embedded into your application, a
shared library build of R is required. This works on Linux, OS X and even
on Windows provided you use the same tools used to build R itself. d
Numerous examples are provided in the eight subdirectories of the
examples/ directory of the installed package: standard, 'mpi' (for
parallel computing), 'qt' (showing how to embed 'RInside' inside a Qt GUI
application), 'wt' (showing how to build a "web-application" using the Wt
toolkit), 'armadillo' (for 'RInside' use with 'RcppArmadillo') and 'eigen'
(for 'RInside' use with 'RcppEigen').  The examples use 'GNUmakefile(s)'
with GNU extensions, so a GNU make is required (and will use the
'GNUmakefile' automatically). 'Doxygen'-generated documentation of the C++
classes is available at the 'RInside' website as well.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/THANKS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%doc %{rlibdir}/%{packname}/lib
