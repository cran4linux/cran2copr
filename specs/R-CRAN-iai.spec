%global packname  iai
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Interface to 'Interpretable AI' Modules

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-JuliaCall 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-JuliaCall 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 

%description
An interface to the algorithms of 'Interpretable AI'
<https://www.interpretable.ai> from the R programming language.
'Interpretable AI' provides various modules, including 'Optimal Trees' for
classification, regression, prescription and survival analysis, 'Optimal
Imputation' for missing data imputation and outlier detection, and
'Optimal Feature Selection' for exact sparse regression. The 'iai' package
is an open-source project. The 'Interpretable AI' software modules are
proprietary products, but free academic and evaluation licenses are
available.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/julia
%{rlibdir}/%{packname}/INDEX
