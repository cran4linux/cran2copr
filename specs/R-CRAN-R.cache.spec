%global packname  R.cache
%global packver   0.14.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14.0
Release:          2%{?dist}
Summary:          Fast and Light-Weight Caching (Memoization) of Objects andResults to Speed Up Computations

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils >= 2.8.0
BuildRequires:    R-CRAN-R.methodsS3 >= 1.7.1
BuildRequires:    R-CRAN-R.oo >= 1.23.0
BuildRequires:    R-CRAN-digest >= 0.6.13
BuildRequires:    R-utils 
Requires:         R-CRAN-R.utils >= 2.8.0
Requires:         R-CRAN-R.methodsS3 >= 1.7.1
Requires:         R-CRAN-R.oo >= 1.23.0
Requires:         R-CRAN-digest >= 0.6.13
Requires:         R-utils 

%description
Memoization can be used to speed up repetitive and computational expensive
function calls.  The first time a function that implements memoization is
called the results are stored in a cache memory.  The next time the
function is called with the same set of parameters, the results are
momentarily retrieved from the cache avoiding repeating the calculations.
With this package, any R object can be cached in a key-value storage where
the key can be an arbitrary set of R objects.  The cache memory is
persistent (on the file system).

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
%doc %{rlibdir}/%{packname}/_Rcache
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
