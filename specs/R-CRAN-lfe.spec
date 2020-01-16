%global packname  lfe
%global packver   2.8-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.5
Release:          1%{?dist}
Summary:          Linear Group Fixed Effects

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.2
Requires:         R-core >= 2.15.2
BuildRequires:    R-Matrix >= 1.1.2
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-parallel 
Requires:         R-Matrix >= 1.1.2
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-xtable 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-sandwich 
Requires:         R-parallel 

%description
Transforms away factors with many levels prior to doing an OLS. Useful for
estimating linear models with multiple group fixed effects, and for
estimating linear models which uses factors with many levels as pure
control variables. Includes support for instrumental variables,
conditional F statistics for weak instruments, robust and multi-way
clustered standard errors, as well as limited mobility bias correction.

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
%doc %{rlibdir}/%{packname}/exec
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
