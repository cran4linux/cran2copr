%global packname  odin
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          ODE Generation and Integration

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cinterpolate >= 1.0.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ring 
Requires:         R-CRAN-cinterpolate >= 1.0.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ring 

%description
Generate systems of ordinary differential equations (ODE) and integrate
them, using a domain specific language (DSL).  The DSL uses R's syntax,
but compiles to C in order to efficiently solve the system.  A solver is
not provided, but instead interfaces to the packages 'deSolve' and 'dde'
are generated.  With these, while solving the differential equations, no
allocations are done and the calculations remain entirely in compiled
code.  Alternatively, a model can be transpiled to R for use in contexts
where a C compiler is not present.  After compilation, models can be
inspected to return information about parameters and outputs, or
intermediate values after calculations. 'odin' is not targeted at any
particular domain and is suitable for any system that can be expressed
primarily as mathematical expressions.  Additional support is provided for
working with delays (delay differential equations, DDE), using
interpolated functions during interpolation, and for integrating
quantities that represent arrays.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/library.c
%doc %{rlibdir}/%{packname}/schema.json
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
