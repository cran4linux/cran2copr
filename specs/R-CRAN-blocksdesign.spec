%global packname  blocksdesign
%global packver   3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5
Release:          1%{?dist}
Summary:          Nested and Crossed Block Designs for Factorial, FractionalFactorial and Unstructured Treatment Sets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-crossdes 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-crossdes 

%description
Constructs D-optimal or near D-optimal nested and crossed block designs
for unstructured or general factorial treatment designs. The treatment
design, if required, is found from a model matrix design formula and can
be added sequentially, if required. The block design is found from a
defined set of block factors and is conditional on the defined treatment
design. The block factors are added in sequence and each added block
factor is optimized conditional on all previously added block factors. The
block design can have repeated nesting down to any required depth of
nesting with either simple nested blocks or a crossed blocks design at
each level of nesting. Outputs include a table showing the allocation of
treatments to blocks and tables showing the achieved D-efficiency factors
for each block and treatment design.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
