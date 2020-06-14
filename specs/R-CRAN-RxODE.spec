%global packname  RxODE
%global packver   0.9.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2.0
Release:          2%{?dist}
Summary:          Facilities for Simulating from ODE-Based Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.300.2.0
BuildRequires:    R-CRAN-units >= 0.6.0
BuildRequires:    R-CRAN-PreciseSums >= 0.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-dparser >= 0.1.8
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-inline 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-rex 
BuildRequires:    R-CRAN-sys 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-lotri 
Requires:         R-CRAN-units >= 0.6.0
Requires:         R-CRAN-PreciseSums >= 0.3
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-dparser >= 0.1.8
Requires:         R-CRAN-knitr 
Requires:         R-Matrix 
Requires:         R-CRAN-brew 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-inline 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-rex 
Requires:         R-CRAN-sys 
Requires:         R-utils 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-lotri 

%description
Facilities for running simulations from ordinary differential equation
(ODE) models, such as pharmacometrics and other compartmental models.  A
compilation manager translates the ODE model into C, compiles it, and
dynamically loads the object code into R for improved computational
efficiency.  An event table object facilitates the specification of
complex dosing regimens (optional) and sampling schedules.  NB: The use of
this package requires both C and Fortran compilers, for details on their
use with R please see Section 6.3, Appendix A, and Appendix D in the "R
Administration and Installation" manual. Also the code is mostly released
under GPL.  The VODE and LSODA are in the public domain.  The information
is available in the inst/COPYRIGHTS. You can also obtain the archived
SnakeCharmR for python integration from CRAN archives
<https://cran.r-project.org/src/contrib/Archive/SnakeCharmR/> or
<https://github.com/nlmixrdevelopment/SnakeCharmR>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/Changes.txt
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/THANKS
%doc %{rlibdir}/%{packname}/tools
%doc %{rlibdir}/%{packname}/tran.g
%doc %{rlibdir}/%{packname}/tutorials
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
