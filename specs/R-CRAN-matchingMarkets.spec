%global __brp_check_rpaths %{nil}
%global packname  matchingMarkets
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Stable Matchings

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppProgress >= 0.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RcppProgress >= 0.2
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-lpSolve 
Requires:         R-lattice 
Requires:         R-CRAN-partitions 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements structural estimators to correct for the sample selection bias
from observed outcomes in matching markets. This includes one-sided
matching of agents into groups as well as two-sided matching of students
to schools. The package also contains algorithms to find stable matchings
in the three most common matching problems: the stable roommates problem,
the college admissions problem, and the house allocation problem.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
