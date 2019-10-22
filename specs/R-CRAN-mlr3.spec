%global packname  mlr3
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Machine Learning in R - Next Generation

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.9.3
BuildRequires:    R-CRAN-lgr >= 0.3.0
BuildRequires:    R-CRAN-mlr3misc >= 0.1.3
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-mlbench 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-checkmate >= 1.9.3
Requires:         R-CRAN-lgr >= 0.3.0
Requires:         R-CRAN-mlr3misc >= 0.1.3
Requires:         R-CRAN-backports 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-mlbench 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-R6 

%description
Efficient, object-oriented programming on the building blocks of machine
learning. Provides 'R6' objects for tasks, learners, resamplings, and
measures. The package is geared towards scalability and larger datasets by
supporting parallelization and out-of-memory data-backends like databases.
While 'mlr3' focuses on the core computational operations, add-on packages
provide additional functionality.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/testthat
%{rlibdir}/%{packname}/INDEX
