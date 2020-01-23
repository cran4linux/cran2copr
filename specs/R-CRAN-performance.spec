%global packname  performance
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}
Summary:          Assessment of Regression Models Performance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-insight >= 0.8.0
BuildRequires:    R-CRAN-bayestestR >= 0.4.0
Requires:         R-CRAN-insight >= 0.8.0
Requires:         R-CRAN-bayestestR >= 0.4.0

%description
Utilities for computing measures to assess model quality, which are not
directly provided by R's 'base' or 'stats' packages. These include e.g.
measures like r-squared, intraclass correlation coefficient (Nakagawa,
Johnson & Schielzeth (2017) <doi:10.1098/rsif.2017.0213>), root mean
squared error or functions to check models for overdispersion, singularity
or zero-inflation and more. Functions apply to a large variety of
regression models, including generalized linear models, mixed effects
models and Bayesian models.

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
