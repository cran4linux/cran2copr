%global packname  abind
%global packver   1.4-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.5
Release:          3%{?dist}%{?buildtag}
Summary:          Combine Multidimensional Arrays

License:          LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 1.5.0
Requires:         R-core >= 1.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-utils 

%description
Combine multidimensional arrays into a single array. This is a
generalization of 'cbind' and 'rbind'.  Works with vectors, matrices, and
higher-dimensional arrays.  Also provides functions 'adrop', 'asub', and
'afill' for manipulating, extracting and replacing data in arrays.

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
%doc %{rlibdir}/%{packname}/sccversion.txt
%doc %{rlibdir}/%{packname}/svnversion.txt
%{rlibdir}/%{packname}/INDEX
