%global packname  rorutadis
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          2%{?dist}
Summary:          Robust Ordinal Regression UTADIS

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 0.9.3.1
BuildRequires:    R-CRAN-gridExtra >= 0.9
BuildRequires:    R-CRAN-hitandrun >= 0.5.2
BuildRequires:    R-CRAN-Rglpk >= 0.5.1
Requires:         R-CRAN-ggplot2 >= 0.9.3.1
Requires:         R-CRAN-gridExtra >= 0.9
Requires:         R-CRAN-hitandrun >= 0.5.2
Requires:         R-CRAN-Rglpk >= 0.5.1

%description
Implementation of Robust Ordinal Regression for multiple criteria
value-based sorting with preference information provided in form of
possibly imprecise assignment examples, assignment-based pairwise
comparisons, and desired class cardinalities [Kadzinski et al. 2015,
<doi:10.1016/j.ejor.2014.09.050>].

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
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
