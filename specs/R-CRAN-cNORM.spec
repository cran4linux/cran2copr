%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cNORM
%global packver   3.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous Norming

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaps >= 3.1
BuildRequires:    R-CRAN-latticeExtra >= 0.6
BuildRequires:    R-CRAN-lattice >= 0.21
Requires:         R-CRAN-leaps >= 3.1
Requires:         R-CRAN-latticeExtra >= 0.6
Requires:         R-CRAN-lattice >= 0.21

%description
Conventional methods for producing standard scores or percentiles in
psychometrics or biometrics are often plagued with 'jumps' or 'gaps'
(i.e., discontinuities) in norm tables and low confidence for assessing
extreme scores. The continuous norming method introduced by A. Lenhard et
al. (2016, <doi:10.1177/1073191116656437>; 2019,
<doi:10.1371/journal.pone.0222279>; 2021 <doi: 10.1177/0013164420928457>)
estimates percentile development (e. g. over age) and generates continuous
test norm scores on the basis of the raw data from standardization
samples, without requiring assumptions about the distribution of the raw
data: Norm scores are directly established from raw data by modeling the
latter ones as a function of both percentile scores and an explanatory
variable (e.g., age). The method minimizes bias arising from sampling and
measurement error, while handling marked deviations from normality,
addressing bottom or ceiling effects and capturing almost all of the
variance in the original norm data sample. It includes procedures for post
stratification of norm samples to overcome bias in data collection and to
mitigate violations of representativeness. An online demonstration is
available via <https://cnorm.shinyapps.io/cNORM/>.

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
