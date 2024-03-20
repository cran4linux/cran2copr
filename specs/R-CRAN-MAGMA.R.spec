%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MAGMA.R
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          MAny-Group MAtching

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-metafor >= 4.4.0
BuildRequires:    R-parallel >= 4.2.0
BuildRequires:    R-stats >= 4.2.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.4
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-psych >= 2.3.9
BuildRequires:    R-CRAN-janitor >= 2.2.0
BuildRequires:    R-CRAN-robumeta >= 2.1
BuildRequires:    R-CRAN-overlapping >= 2.1
BuildRequires:    R-CRAN-tidyverse >= 2.0.0
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-doParallel >= 1.0.17
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-flextable >= 0.9.4
Requires:         R-CRAN-metafor >= 4.4.0
Requires:         R-parallel >= 4.2.0
Requires:         R-stats >= 4.2.0
Requires:         R-CRAN-ggplot2 >= 3.4.4
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-psych >= 2.3.9
Requires:         R-CRAN-janitor >= 2.2.0
Requires:         R-CRAN-robumeta >= 2.1
Requires:         R-CRAN-overlapping >= 2.1
Requires:         R-CRAN-tidyverse >= 2.0.0
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-doParallel >= 1.0.17
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-flextable >= 0.9.4

%description
Balancing quasi-experimental field research for effects of covariates is
fundamental for drawing causal inference. Propensity Score Matching deals
with this issue but current techniques are restricted to binary treatment
variables. Moreover, they provide several solutions without providing a
comprehensive framework on choosing the best model. The 'MAGMA.R' -package
addresses these restrictions by offering nearest neighbor matching for two
to four groups. It also includes the option to match data of a 2x2 design.
In addition, 'MAGMA.R' includes a framework for evaluating the
post-matching balance. The package includes functions for the matching
process and matching reporting. We provide a tutorial on 'MAGMA.R' as
vignette. More information on 'MAGMA.R' can be found in Feuchter, M. D.,
Urban, J., Scherrer V., Breit, M. L., and Preckel F. (2022)
<https://osf.io/p47nc/>.

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
