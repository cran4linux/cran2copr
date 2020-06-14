%global packname  BB
%global packver   2019.10-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.10.1
Release:          2%{?dist}
Summary:          Solving and Optimizing Large-Scale Nonlinear Systems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.1
Requires:         R-core >= 2.6.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-stats 
Requires:         R-CRAN-quadprog 

%description
Barzilai-Borwein spectral methods for solving nonlinear system of
equations, and for optimizing nonlinear objective functions subject to
simple constraints. A tutorial style introduction to this package is
available in a vignette on the CRAN download page or, when the package is
loaded in an R session, with vignette("BB").

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/slowTests
%{rlibdir}/%{packname}/INDEX
