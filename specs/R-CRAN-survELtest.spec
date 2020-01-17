%global packname  survELtest
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Comparing Multiple Survival Functions with Crossing Hazards

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Iso 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-survival 
BuildRequires:    R-stats 
Requires:         R-CRAN-Iso 
Requires:         R-CRAN-nloptr 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-survival 
Requires:         R-stats 

%description
Computing the one-sided/two-sided integrated/maximally selected EL
statistics for simultaneous testing, the one-sided/two-sided EL tests for
pointwise testing, and an initial test that precedes one-sided testing to
exclude the possibility of crossings or alternative orderings among the
survival functions.

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
