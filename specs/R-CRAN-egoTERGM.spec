%global packname  egoTERGM
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Estimation of Ego-Temporal Exponential Random Graph Models viaExpectation Maximization (EM)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.3.3
BuildRequires:    R-stats >= 3.3.3
BuildRequires:    R-methods >= 3.3.3
BuildRequires:    R-CRAN-ergm >= 3.10.1
BuildRequires:    R-CRAN-sna >= 2.4
BuildRequires:    R-CRAN-btergm >= 1.9.4
BuildRequires:    R-CRAN-xergm.common >= 1.7.7
BuildRequires:    R-CRAN-GGally >= 1.3.2
BuildRequires:    R-boot >= 1.3.18
BuildRequires:    R-Matrix >= 1.2.8
BuildRequires:    R-CRAN-network >= 1.13
BuildRequires:    R-CRAN-speedglm >= 0.3.2
Requires:         R-parallel >= 3.3.3
Requires:         R-stats >= 3.3.3
Requires:         R-methods >= 3.3.3
Requires:         R-CRAN-ergm >= 3.10.1
Requires:         R-CRAN-sna >= 2.4
Requires:         R-CRAN-btergm >= 1.9.4
Requires:         R-CRAN-xergm.common >= 1.7.7
Requires:         R-CRAN-GGally >= 1.3.2
Requires:         R-boot >= 1.3.18
Requires:         R-Matrix >= 1.2.8
Requires:         R-CRAN-network >= 1.13
Requires:         R-CRAN-speedglm >= 0.3.2

%description
Estimation of ego-temporal exponential random graph models with two-stage
estimation including initialization through k-means clustering on temporal
exponential random graph model parameters and EM as per Campbell (2018)
<doi:10.7910/DVN/TWHEZ9>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
