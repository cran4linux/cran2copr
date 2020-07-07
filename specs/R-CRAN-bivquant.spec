%global packname  bivquant
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}
Summary:          Estimation of Bivariate Quantiles

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-regpro 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-MASS 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-regpro 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-copula 
Requires:         R-MASS 

%description
Computation of bivariate quantiles via linear programming based on a novel
direction-based approach using the cumulative distribution function.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
