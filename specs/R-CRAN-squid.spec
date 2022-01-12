%global __brp_check_rpaths %{nil}
%global packname  squid
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Quantification of Individual Differences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.53.1
BuildRequires:    R-CRAN-plotly >= 4.9.3
BuildRequires:    R-grid >= 4.1.1
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-brms >= 2.15.0
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-arm >= 1.10.1
BuildRequires:    R-CRAN-data.table >= 1.1.27.1
BuildRequires:    R-CRAN-lme4 >= 1.1.21
BuildRequires:    R-CRAN-shinyMatrix >= 0.4.0
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS >= 7.3.53.1
Requires:         R-CRAN-plotly >= 4.9.3
Requires:         R-grid >= 4.1.1
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-brms >= 2.15.0
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-arm >= 1.10.1
Requires:         R-CRAN-data.table >= 1.1.27.1
Requires:         R-CRAN-lme4 >= 1.1.21
Requires:         R-CRAN-shinyMatrix >= 0.4.0
Requires:         R-stats 

%description
A simulation-based tool made to help researchers to become familiar with
multilevel variations, and to build up sampling designs for their study.
This tool has two main objectives: First, it provides an educational tool
useful for students, teachers and researchers who want to learn to use
mixed-effects models. Users can experience how the mixed-effects model
framework can be used to understand distinct biological phenomena by
interactively exploring simulated multilevel data. Second, it offers
research opportunities to those who are already familiar with
mixed-effects models, as it enables the generation of data sets that users
may download and use for a range of simulation-based statistical analyses
such as power and sensitivity analysis of multilevel and multivariate data
[Allegue, H., Araya-Ajoy, Y.G., Dingemanse, N.J., Dochtermann N.A.,
Garamszegi, L.Z., Nakagawa, S., Reale, D., Schielzeth, H. and Westneat,
D.F. (2016) <doi: 10.1111/2041-210X.12659>].

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
