%global packname  pCODE
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          2%{?dist}
Summary:          Estimation of an Ordinary Differential Equation Model byParameter Cascade Method

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-base 
BuildRequires:    R-stats 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-pracma 
Requires:         R-MASS 
Requires:         R-CRAN-deSolve 
Requires:         R-base 
Requires:         R-stats 

%description
An implementation of the parameter cascade method Ramsay, J. O.,
Hooker,G., Campbell, D., and Cao, J. (2007)
<doi:10.1111/j.1467-9868.2007.00610.x> for estimating ordinary
differential equation models with missing or complete observations. It
combines smoothing method and profile estimation to estimate any
non-linear dynamic system. The package also offers variance estimates for
parameters of interest based on either bootstrap or Delta method.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
