%global packname  parallelSVM
%global packver   0.1-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          2%{?dist}
Summary:          A Parallel-Voting Version of the Support-Vector-MachineAlgorithm

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.1.1
BuildRequires:    R-CRAN-e1071 >= 1.6.3
BuildRequires:    R-CRAN-foreach >= 1.2.0
BuildRequires:    R-CRAN-doParallel >= 1.0.8
Requires:         R-parallel >= 3.1.1
Requires:         R-CRAN-e1071 >= 1.6.3
Requires:         R-CRAN-foreach >= 1.2.0
Requires:         R-CRAN-doParallel >= 1.0.8

%description
By sampling your data, running the Support-Vector-Machine algorithm on
these samples in parallel on your own machine and letting your models vote
on a prediction, we return much faster predictions than the regular
Support-Vector-Machine and possibly even more accurate predictions.

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
%{rlibdir}/%{packname}/INDEX
