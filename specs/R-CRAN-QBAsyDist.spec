%global packname  QBAsyDist
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Asymmetric Distributions and Quantile Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.38
BuildRequires:    R-CRAN-Deriv >= 3.8.5
BuildRequires:    R-CRAN-GoFKernel >= 2.1.1
BuildRequires:    R-CRAN-nloptr >= 1.2.1
BuildRequires:    R-CRAN-ald >= 1.2
BuildRequires:    R-CRAN-scdensity >= 1.0.2
BuildRequires:    R-CRAN-locpol >= 0.7.0
BuildRequires:    R-CRAN-zipfR >= 0.6.10
Requires:         R-CRAN-quantreg >= 5.38
Requires:         R-CRAN-Deriv >= 3.8.5
Requires:         R-CRAN-GoFKernel >= 2.1.1
Requires:         R-CRAN-nloptr >= 1.2.1
Requires:         R-CRAN-ald >= 1.2
Requires:         R-CRAN-scdensity >= 1.0.2
Requires:         R-CRAN-locpol >= 0.7.0
Requires:         R-CRAN-zipfR >= 0.6.10

%description
Provides the local polynomial maximum likelihood estimates for the
location and scale functions as well as the semiparametric quantile
estimates in the generalized quantile-based asymmetric distributional
setting. These functions are useful for any member of the generalized
quantile-based asymmetric family of distributions.

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
