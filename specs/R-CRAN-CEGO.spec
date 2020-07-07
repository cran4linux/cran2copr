%global packname  CEGO
%global packver   2.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0
Release:          3%{?dist}
Summary:          Combinatorial Efficient Global Optimization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ParamHelpers 
BuildRequires:    R-CRAN-fastmatch 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-DEoptim 
Requires:         R-graphics 
Requires:         R-CRAN-quadprog 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-ParamHelpers 
Requires:         R-CRAN-fastmatch 

%description
Model building, surrogate model based optimization and Efficient Global
Optimization in combinatorial or mixed search spaces.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
