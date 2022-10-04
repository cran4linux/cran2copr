%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidycmprsk
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Competing Risks Estimation

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-tibble >= 3.1.6
BuildRequires:    R-CRAN-cli >= 3.1.0
BuildRequires:    R-CRAN-cmprsk >= 2.2.10
BuildRequires:    R-CRAN-gtsummary >= 1.6.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-broom >= 1.0.1
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-hardhat >= 0.2.0
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-tibble >= 3.1.6
Requires:         R-CRAN-cli >= 3.1.0
Requires:         R-CRAN-cmprsk >= 2.2.10
Requires:         R-CRAN-gtsummary >= 1.6.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-broom >= 1.0.1
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-hardhat >= 0.2.0
Requires:         R-CRAN-survival 

%description
Provides an intuitive interface for working with the competing risk
endpoints. The package wraps the 'cmprsk' package, and exports functions
for univariate cumulative incidence estimates and competing risk
regression. Methods follow those introduced in Fine and Gray (1999)
<doi:10.1002/sim.7501>.

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
