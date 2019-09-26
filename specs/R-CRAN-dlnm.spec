%global packname  dlnm
%global packver   2.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.9
Release:          1%{?dist}
Summary:          Distributed Lag Non-Linear Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-splines 
BuildRequires:    R-nlme 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-tsModel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-splines 
Requires:         R-nlme 
Requires:         R-mgcv 
Requires:         R-CRAN-tsModel 

%description
Collection of functions for distributed lag linear and non-linear models.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/Changesince151
%doc %{rlibdir}/%{packname}/Changesince200
%doc %{rlibdir}/%{packname}/Changesince220
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
