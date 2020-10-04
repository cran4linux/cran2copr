%global packname  PAWL
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Implementation of the PAWL algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-ggplot2 

%description
Implementation of the Parallel Adaptive Wang-Landau algorithm. Also
implemented for comparison: parallel adaptive Metropolis-Hastings,SMC
sampler.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/gpriorexample.R
%doc %{rlibdir}/%{packname}/isingexample.R
%doc %{rlibdir}/%{packname}/mixture4kexamplegoodinit.R
%doc %{rlibdir}/%{packname}/trimodalexample.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
