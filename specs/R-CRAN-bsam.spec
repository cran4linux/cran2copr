%global __brp_check_rpaths %{nil}
%global packname  bsam
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian State-Space Models for Animal Movement

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.10
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-msm >= 1.6.8
BuildRequires:    R-CRAN-sp >= 1.2.3
BuildRequires:    R-CRAN-mvtnorm >= 1.1.1
BuildRequires:    R-CRAN-rworldxtra >= 1.01
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-coda >= 0.19.3
Requires:         R-CRAN-rjags >= 4.10
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-msm >= 1.6.8
Requires:         R-CRAN-sp >= 1.2.3
Requires:         R-CRAN-mvtnorm >= 1.1.1
Requires:         R-CRAN-rworldxtra >= 1.01
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-coda >= 0.19.3

%description
Tools to fit Bayesian state-space models to animal tracking data. Models
are provided for location filtering, location filtering and behavioural
state estimation, and their hierarchical versions. The models are
primarily intended for fitting to ARGOS satellite tracking data but
options exist to fit to other tracking data types. For Global Positioning
System data, consider the 'moveHMM' package. Simplified Markov Chain Monte
Carlo convergence diagnostic plotting is provided but users are encouraged
to explore tools available in packages such as 'coda' and 'boa'.

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
