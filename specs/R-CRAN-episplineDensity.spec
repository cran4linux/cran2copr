%global packname  episplineDensity
%global packver   0.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          Density Estimation with Soft Information by ExponentialEpi-splines

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-pracma 

%description
Produce one-dimensional density estimates using exponential epi-splines.
The user may incorporate soft information, by imposing constraints that
(i) require unimodality; (ii) require that the density be monotone
non-increase or non-decreasing; (iii) put upper bounds on first or second
moments; (iv) bound the density's values at mesh points; (v) require that
the estimate be continuous or continuously differentiable; and more.

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
