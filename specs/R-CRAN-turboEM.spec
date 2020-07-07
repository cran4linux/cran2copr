%global packname  turboEM
%global packver   2020.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2020.1
Release:          3%{?dist}
Summary:          A Suite of Convergence Acceleration Schemes for EM, MM and OtherFixed-Point Algorithms

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-iterators 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-iterators 

%description
Algorithms for accelerating the convergence of slow, monotone sequences
from smooth, contraction mapping such as the EM and MM algorithms. It can
be used to accelerate any smooth, linearly convergent acceleration scheme.
A tutorial style introduction to this package is available in a vignette
on the CRAN download page or, when the package is loaded in an R session,
with vignette("turboEM").

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
