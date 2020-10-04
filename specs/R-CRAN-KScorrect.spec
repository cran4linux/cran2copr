%global packname  KScorrect
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Lilliefors-Corrected Kolmogorov-Smirnov Goodness-of-Fit Tests

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.0
BuildRequires:    R-CRAN-mclust >= 5.4
BuildRequires:    R-parallel >= 3.6.0
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-doParallel >= 1.0.14
BuildRequires:    R-CRAN-iterators >= 1.0.10
Requires:         R-MASS >= 7.3.0
Requires:         R-CRAN-mclust >= 5.4
Requires:         R-parallel >= 3.6.0
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-doParallel >= 1.0.14
Requires:         R-CRAN-iterators >= 1.0.10

%description
Implements the Lilliefors-corrected Kolmogorov-Smirnov test for use in
goodness-of-fit tests, suitable when population parameters are unknown and
must be estimated by sample statistics. P-values are estimated by
simulation. Can be used with a variety of continuous distributions,
including normal, lognormal, univariate mixtures of normals, uniform,
loguniform, exponential, gamma, and Weibull distributions. Functions to
generate random numbers and calculate density, distribution, and quantile
functions are provided for use with the log uniform and mixture
distributions.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
