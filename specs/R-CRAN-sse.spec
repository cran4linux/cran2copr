%global packname  sse
%global packver   0.7-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.15
Release:          1%{?dist}
Summary:          Sample Size Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-lattice 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-lattice 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-parallel 

%description
Provides functions to evaluate user-defined power functions for a
parameter range, and draws a sensitivity plot. It also provides a
resampling procedure for semi-parametric sample size estimation and
methods for adding information to a Sweave report.

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
%doc %{rlibdir}/%{packname}/slowTests
%{rlibdir}/%{packname}/INDEX
