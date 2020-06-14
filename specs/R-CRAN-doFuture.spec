%global packname  doFuture
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          2%{?dist}
Summary:          A Universal Foreach Parallel Adapter using the Future API of the'future' Package

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach >= 1.4.7
BuildRequires:    R-CRAN-future >= 1.15.1
BuildRequires:    R-CRAN-iterators >= 1.0.12
BuildRequires:    R-CRAN-globals >= 0.12.5
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
Requires:         R-CRAN-foreach >= 1.4.7
Requires:         R-CRAN-future >= 1.15.1
Requires:         R-CRAN-iterators >= 1.0.12
Requires:         R-CRAN-globals >= 0.12.5
Requires:         R-parallel 
Requires:         R-utils 

%description
Provides a '%dopar%' adapter such that any type of futures can be used as
backends for the 'foreach' framework.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/tests2
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
