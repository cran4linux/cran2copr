%global packname  jsr223
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          A 'Java' Platform Integration for 'R' with Programming Languages'Groovy', 'JavaScript', 'JRuby' ('Ruby'), 'Jython' ('Python'),and 'Kotlin'

License:          GPL (>= 2) | BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils >= 3.3.0
BuildRequires:    R-CRAN-curl >= 3.0
BuildRequires:    R-CRAN-R6 >= 2.2.0
BuildRequires:    R-CRAN-rJava >= 0.9.8
BuildRequires:    R-CRAN-jdx >= 0.1.0
Requires:         R-utils >= 3.3.0
Requires:         R-CRAN-curl >= 3.0
Requires:         R-CRAN-R6 >= 2.2.0
Requires:         R-CRAN-rJava >= 0.9.8
Requires:         R-CRAN-jdx >= 0.1.0

%description
Provides a high-level integration for the 'Java' platform that makes
'Java' objects easy to use from within 'R'; provides a unified interface
to integrate 'R' with several programming languages; and features
extensive data exchange between 'R' and 'Java'. The 'jsr223'-supported
programming languages include 'Groovy', 'JavaScript', 'JRuby' ('Ruby'),
'Jython' ('Python'), and 'Kotlin'. Any of these languages can use and
extend 'Java' classes in natural syntax. Furthermore, solutions developed
in any of the 'jsr223'-supported languages are also accessible to 'R'
developers. The 'jsr223' package also features callbacks, script
compiling, and string interpolation. In all, 'jsr223' significantly
extends the computing capabilities of the 'R' software environment.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
