%global packname  lbfgsb3
%global packver   2015-2.13.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2015.2.13.1
Release:          1%{?dist}
Summary:          Limited Memory BFGS Minimizer with Bounds on Parameters

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-numDeriv 

%description
Interfacing to Nocedal et al. L-BFGS-B.3.0 (2011) limited memory BFGS
minimizer with bounds on parameters.

%prep
%setup -q -c -n %{packname}


%build

%install
test $(gcc -dumpversion) -ge 10 && export PKG_FFLAGS=-fallow-argument-mismatch
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
%doc %{rlibdir}/%{packname}/drlbfgsb3.R
%doc %{rlibdir}/%{packname}/lbfgsb140731.f
%doc %{rlibdir}/%{packname}/License-lbfgsb-orig.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
