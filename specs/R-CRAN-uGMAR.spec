%global __brp_check_rpaths %{nil}
%global packname  uGMAR
%global packver   3.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Univariate Gaussian and Student's t Mixture Autoregressive Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.3.2
BuildRequires:    R-CRAN-gsl >= 1.9.10.3
BuildRequires:    R-CRAN-pbapply >= 1.3.2
BuildRequires:    R-CRAN-Brobdingnag >= 1.2.4
BuildRequires:    R-parallel 
Requires:         R-stats >= 3.3.2
Requires:         R-CRAN-gsl >= 1.9.10.3
Requires:         R-CRAN-pbapply >= 1.3.2
Requires:         R-CRAN-Brobdingnag >= 1.2.4
Requires:         R-parallel 

%description
Maximum likelihood estimation of univariate Gaussian Mixture
Autoregressive (GMAR), Student's t Mixture Autoregressive (StMAR), and
Gaussian and Student's t Mixture Autoregressive (G-StMAR) models, quantile
residual tests, graphical diagnostics, forecast and simulate from GMAR,
StMAR and G-StMAR processes. Leena Kalliovirta, Mika Meitz, Pentti
Saikkonen (2015) <doi:10.1111/jtsa.12108>, Mika Meitz, Daniel Preve,
Pentti Saikkonen (2021) <doi:10.1080/03610926.2021.1916531>, Savi
Virolainen (2021) <doi:10.1515/snde-2020-0060>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
