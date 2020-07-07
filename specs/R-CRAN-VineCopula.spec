%global packname  VineCopula
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          3%{?dist}
Summary:          Statistical Inference of Vine Copulas

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ADGofTest 
BuildRequires:    R-lattice 
BuildRequires:    R-parallel 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-methods 
Requires:         R-CRAN-ADGofTest 
Requires:         R-lattice 
Requires:         R-parallel 

%description
Provides tools for the statistical analysis of vine copula models. The
package includes tools for parameter estimation, model selection,
simulation, goodness-of-fit tests, and visualization. Tools for
estimation, selection and exploratory data analysis of bivariate copula
models are also provided.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
