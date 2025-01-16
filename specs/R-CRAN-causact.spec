%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  causact
%global packver   0.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.7
Release:          1%{?dist}%{?buildtag}
Summary:          Fast, Easy, and Visual Bayesian Inference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.1
BuildRequires:    R-CRAN-reticulate >= 1.30
BuildRequires:    R-CRAN-igraph >= 1.2.7
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-cowplot >= 1.1.0
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.9
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-lifecycle >= 1.0.2
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-forcats >= 0.5.0
BuildRequires:    R-CRAN-rstudioapi >= 0.11
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.1
Requires:         R-CRAN-reticulate >= 1.30
Requires:         R-CRAN-igraph >= 1.2.7
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-cowplot >= 1.1.0
Requires:         R-CRAN-DiagrammeR >= 1.0.9
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-lifecycle >= 1.0.2
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-forcats >= 0.5.0
Requires:         R-CRAN-rstudioapi >= 0.11

%description
Accelerate Bayesian analytics workflows in 'R' through interactive
modelling, visualization, and inference. Define probabilistic graphical
models using directed acyclic graphs (DAGs) as a unifying language for
business stakeholders, statisticians, and programmers. This package relies
on interfacing with the 'numpyro' python package.

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
