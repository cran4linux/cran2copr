%global __brp_check_rpaths %{nil}
%global packname  FlexParamCurve
%global packver   1.5-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5
Release:          3%{?dist}%{?buildtag}
Summary:          Tools to Fit Flexible Parametric Curves

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-nlme 
Requires:         R-stats 
Requires:         R-utils 

%description
Model selection tools and 'selfStart' functions to fit parametric curves
in 'nls', 'nlsList' and 'nlme' frameworks.

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
