%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AIBias
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Longitudinal Bias Auditing for Sequential Decision Systems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.0

%description
Provides tools for detecting, quantifying, and visualizing algorithmic
bias as a longitudinal process in repeated decision systems. Existing
fairness metrics treat bias as a single-period snapshot; this package
operationalizes the view that bias in sequential systems must be measured
over time. Implements group-specific decision-rate trajectories,
standardized disparity measures analogous to the standardized mean
difference (Cohen, 1988, ISBN:0-8058-0283-5), cumulative bias burden,
Markov-based transition disparity (recovery and retention gaps), and a
dynamic amplification index that quantifies whether prior decisions
compound current group inequality. The amplification framework extends
longitudinal causal inference ideas from Robins (1986)
<doi:10.1016/0270-0255(86)90088-6> and the sequential decision-process
perspective in the fairness literature (see <https://fairmlbook.org>) to
the audit setting. Covariate-adjusted trajectories are estimated via
logistic regression, generalized additive models (Wood, 2017,
<doi:10.1201/9781315370279>), or generalized linear mixed models (Bates,
2015, <doi:10.18637/jss.v067.i01>). Uncertainty quantification uses the
cluster bootstrap (Cameron, 2008, <doi:10.1162/rest.90.3.414>).

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
