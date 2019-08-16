%global packname  rJava
%global packver   0.9-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.11
Release:          1%{?dist}
Summary:          Low-Level R to Java Interface

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-java-devel
BuildRequires:    make
Requires:         java
BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Low-level interface to Java VM very much like .C/.Call and friends. Allows
creation of objects, calling methods and accessing fields.

%prep
%setup -q -c -n %{packname}


%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD javareconf -e '%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}'
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/javadoc
%doc %{rlibdir}/%{packname}/jri
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
