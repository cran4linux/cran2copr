%global packname  DynamicGP
%global packver   1.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}
Summary:          Modelling and Analysis of Dynamic Computer Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-lhs 
Requires:         R-parallel 
Requires:         R-stats 

%description
Emulating and solving inverse problems for dynamic computer experiments.
It contains two major functionalities: (1) localized GP model for
large-scale dynamic computer experiments using the algorithm proposed by
Zhang et al. (2018) <arXiv:1611.09488>; (2) solving inverse problems in
dynamic computer experiments. The current version only supports 64-bit
version of R.

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
%doc %{rlibdir}/%{packname}/config.r
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
