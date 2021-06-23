%global __brp_check_rpaths %{nil}
%global packname  clusteredinterference
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Causal Effects from Observational Studies with ClusteredInterference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv >= 2014.2.1
BuildRequires:    R-CRAN-rootSolve >= 1.6.6
BuildRequires:    R-CRAN-Formula >= 1.1.2
BuildRequires:    R-CRAN-cubature >= 1.1.2
BuildRequires:    R-CRAN-lme4 >= 1.1.10
Requires:         R-CRAN-numDeriv >= 2014.2.1
Requires:         R-CRAN-rootSolve >= 1.6.6
Requires:         R-CRAN-Formula >= 1.1.2
Requires:         R-CRAN-cubature >= 1.1.2
Requires:         R-CRAN-lme4 >= 1.1.10

%description
Estimating causal effects from observational studies assuming clustered
(or partial) interference. These inverse probability-weighted estimators
target new estimands arising from population-level treatment policies. The
estimands and estimators are introduced in Barkley et al. (2017)
<arXiv:1711.04834>.

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
