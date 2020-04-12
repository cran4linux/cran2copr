%global packname  Cyclops
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}
Summary:          Cyclic Coordinate Descent for Logistic, Poisson and SurvivalAnalysis

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-BH >= 1.51.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-bit 
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-CRAN-ffbase 
BuildRequires:    R-methods 
BuildRequires:    R-survival 
BuildRequires:    R-MASS 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-Matrix 
Requires:         R-CRAN-bit 
Requires:         R-CRAN-ff 
Requires:         R-CRAN-ffbase 
Requires:         R-methods 
Requires:         R-survival 
Requires:         R-MASS 

%description
This model fitting tool incorporates cyclic coordinate descent and
majorization-minimization approaches to fit a variety of regression models
found in large-scale observational healthcare data.  Implementations focus
on computational optimization and fine-scale parallelization to yield
efficient inference in massive datasets.  Please see: Suchard, Simpson,
Zorych, Ryan and Madigan (2013) <doi:10.1145/2414416.2414791>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
