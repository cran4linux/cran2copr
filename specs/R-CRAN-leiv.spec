%global __brp_check_rpaths %{nil}
%global packname  leiv
%global packver   2.0-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.7
Release:          3%{?dist}%{?buildtag}
Summary:          Bivariate Linear Errors-In-Variables Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 

%description
Estimate the slope and intercept of a bivariate linear relationship by
calculating a posterior density that is invariant to interchange and
scaling of the coordinates.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
