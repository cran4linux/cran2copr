%global packname  optinterv
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Optimal Intervention

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-distances 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-boot 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-distances 
Requires:         R-CRAN-weights 
Requires:         R-boot 
Requires:         R-lattice 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 
Requires:         R-graphics 

%description
Provides both parametric and non-parametric estimates of the correlates of
some desired outcome (e.g. test scores, income) using a new method
proposed by Danieli, Devi and Fryer (2019). This method relaxes the
assumption that one can alter individual characteristics in any way the
data suggest is optimal, and so can be used anytime one wants to use
observational data to better optimize social experiments designed to
increase some desired outcome.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
