%global packname  spatstat.sparse
%global packver   1.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Sparse Three-Dimensional Arrays and Linear Algebra Utilities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-spatstat.utils >= 1.17.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-tensor 
Requires:         R-CRAN-spatstat.utils >= 1.17.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-tensor 

%description
Defines sparse three-dimensional arrays and supports standard operations
on them. The package also includes utility functions for matrix
calculations that are common in statistics, such as quadratic forms.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
