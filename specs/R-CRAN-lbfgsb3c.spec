%global packname  lbfgsb3c
%global packver   2020-3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2020.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Limited Memory BFGS Minimizer with Bounds on Parameters withoptim() 'C' Interface

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-numDeriv 
Requires:         R-methods 

%description
Interfacing to Nocedal et al. L-BFGS-B.3.0 (See
<http://users.iems.northwestern.edu/~nocedal/lbfgsb.html>) limited memory
BFGS minimizer with bounds on parameters. This is a fork of 'lbfgsb3'.
This registers a 'R' compatible 'C' interface to L-BFGS-B.3.0 that uses
the same function types and optimization as the optim() function (see
writing 'R' extensions and source for details).  This package also adds
more stopping criteria as well as allowing the adjustment of more
tolerances.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && echo "FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch" > ~/.R/Makevars
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
%doc %{rlibdir}/%{packname}/drlbfgsb3.R
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/lbfgsb140731.f
%doc %{rlibdir}/%{packname}/License-lbfgsb-orig.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
