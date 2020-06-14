%global packname  iZID
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          Identify Zero-Inflated Distributions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.1.0
BuildRequires:    R-stats >= 3.1.0
BuildRequires:    R-CRAN-extraDistr >= 1.8.11
BuildRequires:    R-CRAN-rootSolve >= 1.7
BuildRequires:    R-CRAN-foreach >= 1.4.7
BuildRequires:    R-CRAN-doParallel >= 1.0.15
Requires:         R-methods >= 3.1.0
Requires:         R-stats >= 3.1.0
Requires:         R-CRAN-extraDistr >= 1.8.11
Requires:         R-CRAN-rootSolve >= 1.7
Requires:         R-CRAN-foreach >= 1.4.7
Requires:         R-CRAN-doParallel >= 1.0.15

%description
Computes bootstrapped Monte Carlo estimate of p value of
Kolmogorov-Smirnov (KS) test and likelihood ratio test for zero-inflated
count data, based on the work of Aldirawi et al. (2019)
<doi:10.1109/BHI.2019.8834661>. With the package, user can also find tools
to simulate random deviates from zero inflated or hurdle models and obtain
maximum likelihood estimate of unknown parameters in these models.

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
%{rlibdir}/%{packname}/INDEX
