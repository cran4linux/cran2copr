%global packname  lmboot
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}
Summary:          Bootstrap in Linear Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.6.0
BuildRequires:    R-CRAN-evd >= 2.3.0
Requires:         R-stats >= 3.6.0
Requires:         R-CRAN-evd >= 2.3.0

%description
Various efficient and robust bootstrap methods are implemented for linear
models with least squares estimation.  Functions within this package allow
users to create bootstrap sampling distributions for model parameters,
test hypotheses about parameters, and visualize the bootstrap sampling or
null distributions.  Methods implemented for linear models include the
wild bootstrap by Wu (1986) <doi:10.1214/aos/1176350142>, the residual and
paired bootstraps by Efron (1979, ISBN:978-1-4612-4380-9), the delete-1
jackknife by Quenouille (1956) <doi:10.2307/2332914>, and the Bayesian
bootstrap by Rubin (1981) <doi:10.1214/aos/1176345338>.

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
