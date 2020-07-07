%global packname  e1071
%global packver   1.7-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.3
Release:          3%{?dist}
Summary:          Misc Functions of the Department of Statistics, ProbabilityTheory Group (Formerly: E1071), TU Wien

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-class 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-class 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 

%description
Functions for latent class analysis, short time Fourier transform, fuzzy
clustering, support vector machines, shortest path computation, bagged
clustering, naive Bayes classifier, ...

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
