%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rrepest
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          An Analyzer of International Large Scale Assessments in Education

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 4.2.1
BuildRequires:    R-CRAN-tibble >= 3.1.8
BuildRequires:    R-CRAN-labelled >= 2.9.1
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.14.8
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-doParallel >= 1.0.17
BuildRequires:    R-CRAN-flextable >= 0.7.2
BuildRequires:    R-CRAN-officer >= 0.6.2
BuildRequires:    R-CRAN-purrr >= 0.3.4
Requires:         R-parallel >= 4.2.1
Requires:         R-CRAN-tibble >= 3.1.8
Requires:         R-CRAN-labelled >= 2.9.1
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-data.table >= 1.14.8
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-doParallel >= 1.0.17
Requires:         R-CRAN-flextable >= 0.7.2
Requires:         R-CRAN-officer >= 0.6.2
Requires:         R-CRAN-purrr >= 0.3.4

%description
An easy way to analyze international large-scale assessments and surveys
in education or any other dataset that includes replicated weights
(Balanced Repeated Replication (BRR) weights, Jackknife replicate
weights,...) while also allowing for analysis with multiply imputed
variables (plausible values). It supports the estimation of univariate
statistics (e.g. mean, variance, standard deviation, quantiles),
frequencies, correlation, linear regression and any other model already
implemented in R that takes a data frame and weights as parameters. It
also includes options to prepare the results for publication, following
the table formatting standards of the Organization for Economic
Cooperation and Development (OECD).

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
