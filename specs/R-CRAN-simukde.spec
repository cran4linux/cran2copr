%global packname  simukde
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Simulation with Kernel Density Estimation

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-MASS 

%description
Generates random values from a univariate and multivariate continuous
distribution by using kernel density estimation based on a sample. Duong
(2017) <doi:10.18637/jss.v021.i07>, Christian P. Robert and George Casella
(2010 ISBN:978-1-4419-1575-7) <doi:10.1007/978-1-4419-1576-4>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
