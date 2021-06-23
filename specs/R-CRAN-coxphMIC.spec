%global __brp_check_rpaths %{nil}
%global packname  coxphMIC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Sparse Estimation of Cox Proportional Hazards Models viaApproximated Information Criterion

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.2.5
BuildRequires:    R-graphics >= 3.2.5
BuildRequires:    R-utils >= 3.2.5
BuildRequires:    R-CRAN-numDeriv >= 2014.2.1
BuildRequires:    R-survival >= 2.38
Requires:         R-stats >= 3.2.5
Requires:         R-graphics >= 3.2.5
Requires:         R-utils >= 3.2.5
Requires:         R-CRAN-numDeriv >= 2014.2.1
Requires:         R-survival >= 2.38

%description
Sparse estimation for Cox PH models is done via Minimum approximated
Information Criterion (MIC) by Su, Wijayasinghe, Fan, and Zhang (2016)
<DOI:10.1111/biom.12484>. MIC mimics the best subset selection using a
penalized likelihood approach yet with no need of a tuning parameter. The
problem is further reformulated with a re-parameterization step so that it
reduces to one unconstrained non-convex yet smooth programming problem,
which can be solved efficiently. Furthermore, the re-parameterization
tactic yields an additional advantage in terms of circumventing
post-selection inference.

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
