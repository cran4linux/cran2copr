%global packname  sem
%global packver   3.1-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.11
Release:          2%{?dist}
Summary:          Structural Equation Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-mi >= 0.9
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-MASS 
BuildRequires:    R-boot 
BuildRequires:    R-utils 
Requires:         R-CRAN-mi >= 0.9
Requires:         R-stats 
Requires:         R-CRAN-matrixcalc 
Requires:         R-MASS 
Requires:         R-boot 
Requires:         R-utils 

%description
Functions for fitting general linear structural equation models (with
observed and latent variables) using the RAM approach, and for fitting
structural equations in observed-variable models by two-stage least
squares.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
