%global packname  rHpcc
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Interface between HPCC and R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.0
Requires:         R-core >= 2.11.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-XML 
Requires:         R-methods 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-XML 

%description
rHpcc is an R package providing an Interface between R and
HPCC.Familiarity with ECL (Enterprise Control Language) is a must to use
this package.HPCC is a massive parallel-processing computing platform that
solves Big Data problems.ECL is the Enterprise Control Language designed
specifically for huge data projects using the HPCC platform.Its extreme
scalability comes from a design that allows you to leverage every query
you create for re-use in subsequent queries as needed. To do this, ECL
takes a dictionary approach to building queries wherein each ECL
definition defines an Attribute. Each previously defined Attribute can
then be used in succeeding ECL Attribute definitions as the language
extends itself as you use it.

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
