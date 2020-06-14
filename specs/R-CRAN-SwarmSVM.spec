%global packname  SwarmSVM
%global packver   0.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          2%{?dist}
Summary:          Ensemble Learning Algorithms Based on Support Vector Machines

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-checkmate >= 1.6.0
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-LiblineaR 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BBmisc 
Requires:         R-CRAN-checkmate >= 1.6.0
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-LiblineaR 
Requires:         R-Matrix 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-kernlab 
Requires:         R-methods 
Requires:         R-CRAN-BBmisc 

%description
Three ensemble learning algorithms based on support vector machines. They
all train support vector machines on subset of data and combine the
result.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/benchmark
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
