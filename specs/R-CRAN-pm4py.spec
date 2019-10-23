%global packname  pm4py
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Interface to the 'PM4py' Process Mining Library

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.11
BuildRequires:    R-CRAN-bupaR 
BuildRequires:    R-CRAN-petrinetR 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-reticulate >= 1.11
Requires:         R-CRAN-bupaR 
Requires:         R-CRAN-petrinetR 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 

%description
Interface to 'PM4py' <http://pm4py.org>, a process mining library in
'Python'. This package uses the 'reticulate' package to act as a bridge
between 'PM4Py' and the 'R' package 'bupaR'. It provides several process
discovery algorithms, evaluation measures, and alignments.

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
%doc %{rlibdir}/%{packname}/python
%{rlibdir}/%{packname}/INDEX
