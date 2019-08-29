%global packname  extremogram
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Estimation of Extreme Value Dependence for Time Series Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.31
BuildRequires:    R-parallel >= 3.1.1
BuildRequires:    R-boot >= 1.3.11
Requires:         R-MASS >= 7.3.31
Requires:         R-parallel >= 3.1.1
Requires:         R-boot >= 1.3.11

%description
Estimation of the sample univariate, cross and return time extremograms.
The package can also adds empirical confidence bands to each of the
extremogram plots via a permutation procedure under the assumption that
the data are independent. Finally, the stationary bootstrap allows us to
construct credible confidence bands for the extremograms.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
