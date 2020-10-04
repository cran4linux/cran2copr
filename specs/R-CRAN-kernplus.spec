%global packname  kernplus
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          A Kernel Regression-Based Multidimensional Wind Turbine PowerCurve

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-graphics >= 3.3.0
BuildRequires:    R-stats >= 3.3.0
BuildRequires:    R-KernSmooth >= 2.23.15
BuildRequires:    R-CRAN-mixtools >= 1.1.0
BuildRequires:    R-CRAN-circular >= 0.4.7
Requires:         R-graphics >= 3.3.0
Requires:         R-stats >= 3.3.0
Requires:         R-KernSmooth >= 2.23.15
Requires:         R-CRAN-mixtools >= 1.1.0
Requires:         R-CRAN-circular >= 0.4.7

%description
Provides wind energy practitioners with an effective machine
learning-based tool that estimates a multivariate power curve and predicts
the wind power output for a specific environmental condition.

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
