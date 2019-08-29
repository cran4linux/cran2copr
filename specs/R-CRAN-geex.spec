%global packname  geex
%global packver   1.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          1%{?dist}
Summary:          An API for M-Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-methods >= 3.3
BuildRequires:    R-CRAN-numDeriv >= 2014.2.1
BuildRequires:    R-CRAN-rootSolve >= 1.6.6
BuildRequires:    R-Matrix >= 1.2.6
BuildRequires:    R-CRAN-lme4 >= 1.1.12
Requires:         R-methods >= 3.3
Requires:         R-CRAN-numDeriv >= 2014.2.1
Requires:         R-CRAN-rootSolve >= 1.6.6
Requires:         R-Matrix >= 1.2.6
Requires:         R-CRAN-lme4 >= 1.1.12

%description
Provides a general, flexible framework for estimating parameters and
empirical sandwich variance estimator from a set of unbiased estimating
equations (i.e., M-estimation in the vein of Stefanski & Boos (2002)
<doi:10.1198/000313002753631330>). Also provides an API to compute
finite-sample variance corrections.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/create_sample_data.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/logos
%{rlibdir}/%{packname}/INDEX
