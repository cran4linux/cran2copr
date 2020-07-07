%global packname  shinybrms
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          2%{?dist}
Summary:          Graphical User Interface (Shiny App) for Package 'brms'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan >= 2.19.3
BuildRequires:    R-CRAN-brms >= 2.12.0
BuildRequires:    R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-rstan >= 2.19.3
Requires:         R-CRAN-brms >= 2.12.0
Requires:         R-CRAN-shiny >= 1.4.0

%description
A graphical user interface (GUI) for the package 'brms' which allows to
fit Bayesian regression models using 'Stan' (<https://mc-stan.org/>) (more
specifically, using its R interface, the package 'rstan'). The 'shinybrms'
GUI is a 'Shiny' (<https://shiny.rstudio.com/>) app, i.e. it was created
using the package 'shiny'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
