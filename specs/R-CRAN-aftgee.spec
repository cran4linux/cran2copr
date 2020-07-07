%global packname  aftgee
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          2%{?dist}
Summary:          Accelerated Failure Time Model with Generalized EstimatingEquations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-MASS 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-geepack 
Requires:         R-survival 
Requires:         R-CRAN-BB 
Requires:         R-MASS 

%description
A collection of methods for both the rank-based estimates and least-square
estimates to the Accelerated Failure Time (AFT) model. For rank-based
estimation, it provides approaches that include the computationally
efficient Gehan's weight and the general's weight such as the logrank
weight. Details of the rank-based estimation can be found in Chiou et al.
(2014) <doi:10.1007/s11222-013-9388-2> and Chiou et al. (2015)
<doi:10.1002/sim.6415>. For the least-square estimation, the estimating
equation is solved with generalized estimating equations (GEE). Moreover,
in multivariate cases, the dependence working correlation structure can be
specified in GEE's setting. Details on the least-squares estimation can be
found in Chiou et al. (2014) <doi:10.1007/s10985-014-9292-x>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bib
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/JSS-codes.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
