%global packname  gMCP
%global packver   0.8-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.15
Release:          1%{?dist}
Summary:          Graph Based Multiple Comparison Procedures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-multcomp >= 1.1
BuildRequires:    R-CRAN-CommonJavaJars >= 1.0.5
BuildRequires:    R-CRAN-rJava >= 0.6.3
BuildRequires:    R-CRAN-xlsxjars >= 0.6.1
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-PolynomF 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-JavaGD 
BuildRequires:    R-stats4 
Requires:         R-CRAN-multcomp >= 1.1
Requires:         R-CRAN-CommonJavaJars >= 1.0.5
Requires:         R-CRAN-rJava >= 0.6.3
Requires:         R-CRAN-xlsxjars >= 0.6.1
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-PolynomF 
Requires:         R-CRAN-mvtnorm 
Requires:         R-Matrix 
Requires:         R-CRAN-JavaGD 
Requires:         R-stats4 

%description
Functions and a graphical user interface for graphical described multiple
test procedures.

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
%{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/References.html
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
