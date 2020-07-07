%global packname  mexhaz
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          3%{?dist}
Summary:          Mixed Effect Excess Hazard Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-lamW 
Requires:         R-survival 
Requires:         R-CRAN-statmod 
Requires:         R-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-splines 
Requires:         R-CRAN-lamW 

%description
Fit flexible (excess) hazard regression models with the possibility of
including non-proportional effects of covariables and of adding a random
effect at the cluster level (corresponding to a shared frailty).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
