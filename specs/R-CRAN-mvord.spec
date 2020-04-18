%global packname  mvord
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Multivariate Ordinal Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-dfoptim 
Requires:         R-MASS 
Requires:         R-CRAN-pbivnorm 
Requires:         R-stats 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-numDeriv 
Requires:         R-Matrix 

%description
A flexible framework for fitting multivariate ordinal regression models
with composite likelihood methods. Methodological details are given in
Hirk, Hornik, Vana (2020) <doi:10.18637/jss.v093.i04>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
