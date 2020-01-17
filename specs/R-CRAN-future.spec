%global packname  future
%global packver   1.16.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.16.0
Release:          1%{?dist}
Summary:          Unified Parallel and Distributed Processing in R for Everyone

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-listenv >= 0.8.0
BuildRequires:    R-CRAN-globals >= 0.12.5
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
Requires:         R-CRAN-listenv >= 0.8.0
Requires:         R-CRAN-globals >= 0.12.5
Requires:         R-CRAN-digest 
Requires:         R-parallel 
Requires:         R-utils 

%description
The purpose of this package is to provide a lightweight and unified Future
API for sequential and parallel processing of R expression via futures.
The simplest way to evaluate an expression in parallel is to use `x %<-% {
expression }` with `plan(multiprocess)`. This package implements
sequential, multicore, multisession, and cluster futures.  With these, R
expressions can be evaluated on the local machine, in parallel a set of
local machines, or distributed on a mix of local and remote machines.
Extensions to this package implement additional backends for processing
futures via compute cluster schedulers etc. Because of its unified API,
there is no need to modify any code in order switch from sequential on the
local machine to, say, distributed processing on a remote compute cluster.
Another strength of this package is that global variables and functions
are automatically identified and exported as needed, making it
straightforward to tweak existing code to make use of futures.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/vignettes-static
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
