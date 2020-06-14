%global packname  rcdk
%global packver   3.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.0
Release:          2%{?dist}
Summary:          Interface to the 'CDK' Libraries

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rcdklibs >= 2.3
BuildRequires:    R-CRAN-fingerprint 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-itertools 
Requires:         R-CRAN-rcdklibs >= 2.3
Requires:         R-CRAN-fingerprint 
Requires:         R-CRAN-rJava 
Requires:         R-methods 
Requires:         R-CRAN-png 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-itertools 

%description
Allows the user to access functionality in the 'CDK', a Java framework for
chemoinformatics. This allows the user to load molecules, evaluate
fingerprints, calculate molecular descriptors and so on. In addition, the
'CDK' API allows the user to view structures in 2D.

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
%doc %{rlibdir}/%{packname}/cont
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/molfiles
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
