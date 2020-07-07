%global packname  rodd
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}
Summary:          Optimal Discriminating Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-quadprog 
Requires:         R-Matrix 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-matrixcalc 

%description
A collection of functions for numerical construction of optimal
discriminating designs. At the current moment T-optimal designs (which
maximize the lower bound for the power of F-test for regression model
discrimination), KL-optimal designs (for lognormal errors) and their
robust analogues can be calculated with the package.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
