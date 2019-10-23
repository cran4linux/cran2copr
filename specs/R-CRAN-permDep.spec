%global packname  permDep
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Permutation Tests for General Dependent Truncation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-survival 
BuildRequires:    R-parallel 
Requires:         R-CRAN-BB 
Requires:         R-survival 
Requires:         R-parallel 

%description
Implementations of permutation approach to hypothesis testing for
quasi-independence of truncation time and failure time. The implemented
approaches are powerful against non-monotone alternatives and thereby
offer protection against erroneous assumptions of quasi-independence. The
proposed tests use either a conditional or an unconditional method to
evaluate the permutation p-value. The conditional method was first
developed in Tsai (1980) <doi:10.2307/2336059> and Efron and Petrosian
(1992) <doi:10.1086/171931>. The unconditional method provides a valid
approximation to the conditional method, yet computationally simpler and
does not hold fixed the size of each risk sets. Users also have an option
to carry out the proposed permutation tests in a parallel computing
fashion.

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
%{rlibdir}/%{packname}/libs
