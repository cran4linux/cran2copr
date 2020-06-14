%global packname  lme4
%global packver   1.1-23
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.23
Release:          2%{?dist}
Summary:          Linear Mixed-Effects Models using 'Eigen' and S4

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-nlme >= 3.1.123
BuildRequires:    R-Matrix >= 1.2.1
BuildRequires:    R-CRAN-minqa >= 1.1.15
BuildRequires:    R-CRAN-nloptr >= 1.0.4
BuildRequires:    R-CRAN-Rcpp >= 0.10.5
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-splines 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-MASS 
BuildRequires:    R-lattice 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-nlme >= 3.1.123
Requires:         R-Matrix >= 1.2.1
Requires:         R-CRAN-minqa >= 1.1.15
Requires:         R-CRAN-nloptr >= 1.0.4
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-splines 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-MASS 
Requires:         R-lattice 
Requires:         R-boot 
Requires:         R-CRAN-statmod 

%description
Fit linear and generalized linear mixed-effects models. The models and
their components are represented using S4 classes and methods.  The core
computational algorithms are implemented using the 'Eigen' C++ library for
numerical linear algebra and 'RcppEigen' "glue".

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/vignettedata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
