%global packname  wyz.code.metaTesting
%global packver   1.1.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.12
Release:          1%{?dist}
Summary:          Wizardry Code Meta Testing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-data.table >= 1.11.8
BuildRequires:    R-CRAN-wyz.code.offensiveProgramming >= 1.1.17
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-data.table >= 1.11.8
Requires:         R-CRAN-wyz.code.offensiveProgramming >= 1.1.17
Requires:         R-methods 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-crayon 
Requires:         R-utils 
Requires:         R-stats 

%description
Meta testing is the ability to test a function without having to provide
its parameter values. Those values will be generated, based on semantic
naming of parameters, as introduced by package
'wyz.code.offensiveProgramming'. Value generation logic can be completed
with your own data types and generation schemes. This to meet your most
specific requirements and to answer to a wide variety of usages, from
general use case to very specific ones. While using meta testing, it
becomes easier to generate stress test campaigns, non-regression test
campaigns and robustness test campaigns, as generated tests can be saved
and reused from session to session. Main benefits of using
'wyz.code.metaTesting' is ability to discover valid and invalid function
parameter combinations, ability to infer valid parameter values, and to
provide smart summaries that allows you to focus on dysfunctional cases.

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
%doc %{rlibdir}/%{packname}/unit-testing
%{rlibdir}/%{packname}/INDEX
