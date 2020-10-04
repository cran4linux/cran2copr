%global packname  Storm
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Write Storm Bolts in R using the Storm Multi-Language Protocol.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-rjson 
Requires:         R-methods 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-rjson 

%description
Storm is a distributed real-time computation system. Similar to how Hadoop
provides a set of general primitives for doing batch processing, Storm
provides a set of general primitives for doing real-time computation.

Storm includes a "Multi-Language" (or "Multilang") Protocol to allow
implementation of Bolts and Spouts in languages other than Java.  This R
extension provides implementations of utility functions to allow an
application developer to focus on application-specific functionality
rather than Storm/R communications plumbing.

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
