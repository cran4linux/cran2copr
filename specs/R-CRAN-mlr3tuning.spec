%global packname  mlr3tuning
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Tuning for 'mlr3'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.9.4
BuildRequires:    R-CRAN-mlr3misc >= 0.1.7
BuildRequires:    R-CRAN-mlr3 >= 0.1.4
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lgr 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-checkmate >= 1.9.4
Requires:         R-CRAN-mlr3misc >= 0.1.7
Requires:         R-CRAN-mlr3 >= 0.1.4
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lgr 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-R6 

%description
Implements methods for hyperparameter tuning with 'mlr3', e.g. Grid
Search, Random Search, or Simulated Annealing. Various termination
criteria can be set and combined.  The class 'AutoTuner' provides a
convenient way to perform nested resampling in combination with 'mlr3'.

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
%{rlibdir}/%{packname}/INDEX
