%global packname  DoE.MIParray
%global packver   0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13
Release:          3%{?dist}
Summary:          Creation of Arrays by Mixed Integer Programming

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-DoE.base 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-DoE.base 

%description
'CRAN' packages 'DoE.base' and 'Rmosek' and non-'CRAN' package 'gurobi'
are enhanced with functionality for the creation of optimized arrays for
experimentation, where optimization is in terms of generalized minimum
aberration. It is also possible to optimally extend existing arrays to
larger run size. Optimization requires the availability of at least one of
the commercial products 'Gurobi' or 'Mosek' (free academic licenses
available for both). For installing 'Gurobi' and its R package 'gurobi',
follow instructions at <http://www.gurobi.com/downloads/gurobi-optimizer>
and <http://www.gurobi.com/documentation/7.5/refman/r_api_overview.html>
(or higher version). For installing 'Mosek' and its R package 'Rmosek',
follow instructions at <https://www.mosek.com/downloads/> and
<http://docs.mosek.com/8.1/rmosek/install-interface.html>, or use the
functionality in the stump CRAN R package 'Rmosek'.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/testsWithGurobiAndMosek
%{rlibdir}/%{packname}/INDEX
