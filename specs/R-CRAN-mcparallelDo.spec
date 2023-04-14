%global __brp_check_rpaths %{nil}
%global packname  mcparallelDo
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Simplified Interface for Running Commands on ParallelProcesses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.6.3
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-checkmate >= 1.6.3
Requires:         R-parallel 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-R6 

%description
Provides a function that wraps mcparallel() and mccollect() from
'parallel' with temporary variables and a task handler.  Wrapped in this
way the results of an mcparallel() call can be returned to the R session
when the fork is complete without explicitly issuing a specific
mccollect() to retrieve the value. Outside of top-level tasks, multiple
mcparallel() jobs can be retrieved with a single call to
mcparallelDoCheck().

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
