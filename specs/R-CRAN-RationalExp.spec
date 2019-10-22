%global packname  RationalExp
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Rationalizing Rational Expectations. Tests and Deviations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-stats 
Requires:         R-CRAN-snowfall 
Requires:         R-stats 

%description
We implement a test of the rational expectations hypothesis based on the
marginal distributions of realizations and subjective beliefs from
D'Haultfoeuille, Gaillac, and Maurel (2018) <doi:10.3386/w25274>. This
test can be used in cases where realizations and subjective beliefs are
observed in two different datasets that cannot be matched, or when they
are observed in the same dataset. The package also computes the estimator
of the minimal deviations from rational expectations than can be
rationalized by the data.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
