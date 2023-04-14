%global __brp_check_rpaths %{nil}
%global packname  acopula
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          3%{?dist}%{?buildtag}
Summary:          Modelling Dependence with Multivariate Archimax (or anyUser-Defined Continuous) Copulas

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Archimax copulas are mixture of Archimedean and EV copulas. The package
provides definitions of several parametric families of generator and
dependence function, computes CDF and PDF, estimates parameters, tests for
goodness of fit, generates random sample and checks copula properties for
custom constructs. In 2-dimensional case explicit formulas for density are
used, in the contrary to higher dimensions when all derivatives are
linearly approximated. Several non-archimax families (normal, FGM,
Plackett) are provided as well.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
