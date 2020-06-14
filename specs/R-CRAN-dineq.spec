%global packname  dineq
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Decomposition of (Income) Inequality

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.0.3
BuildRequires:    R-boot >= 1.3.20
Requires:         R-CRAN-Hmisc >= 4.0.3
Requires:         R-boot >= 1.3.20

%description
Decomposition of (income) inequality by population sub groups. For a
decomposition on a single variable the mean log deviation can be used (see
Mookherjee Shorrocks (1982) <DOI:10.2307/2232673>). For a decomposition on
multiple variables a regression based technique can be used (see Fields
(2003) <DOI:10.1016/s0147-9121(03)22001-x>). Recentered influence function
regression for marginal effects of the (income or wealth) distribution
(see Firpo et al. (2009) <DOI:10.3982/ECTA6822>). Some extensions to
inequality functions to handle weights and/or missings.

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
