%global __brp_check_rpaths %{nil}
%global packname  investr
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Inverse Estimation/Calibration Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-graphics 
BuildRequires:    R-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-base 
Requires:         R-graphics 
Requires:         R-nlme 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions to facilitate inverse estimation (e.g., calibration) in linear,
generalized linear, nonlinear, and (linear) mixed-effects models. A
generic function is also provided for plotting fitted regression models
with or without confidence/prediction bands that may be of use to the
general user.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
