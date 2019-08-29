%global packname  kantorovich
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Kantorovich Distance Between Probability Measures

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel
Requires:         gmp
BuildRequires:    R-devel >= 2.5.3
Requires:         R-core >= 2.5.3
BuildArch:        noarch
BuildRequires:    R-CRAN-rcdd 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-Rglpk 
Requires:         R-CRAN-rcdd 
Requires:         R-CRAN-gmp 
Requires:         R-methods 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-Rglpk 

%description
Computes the Kantorovich distance between two probability measures on a
finite set.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/local-tests
%{rlibdir}/%{packname}/INDEX
