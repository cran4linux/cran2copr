%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  actisomni
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Sleep Measures of Actigraphy and Activity Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-actibase >= 0.8.0
BuildRequires:    R-CRAN-asleep >= 0.4.0
BuildRequires:    R-CRAN-actiread 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sleeper 
Requires:         R-CRAN-actibase >= 0.8.0
Requires:         R-CRAN-asleep >= 0.4.0
Requires:         R-CRAN-actiread 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-CRAN-sleeper 

%description
Estimates sleep from wrist accelerometry and epoch-level activity data.
Implements sleep-period-time guiders based on angle changes, posture,
least-active periods, sustained inactivity, low activity, and diary or
fixed time windows; combines guider windows with sustained-inactivity
bouts to produce sleep/wake labels and consensus estimates. Provides diary
helpers, and interfaces to the 'asleep' and 'sleeper' machine-learning
estimators. The angle-based and sustained-inactivity methods are described
by van Hees et al. (2015) <doi:10.1371/journal.pone.0142533> and van Hees
et al. (2018) <doi:10.1038/s41598-018-31266-z>; the model estimators are
described by Yuan et al. (2024) <doi:10.1038/s41746-024-01065-0> and
Sundararajan et al. (2021) <doi:10.1038/s41598-020-79217-x>.

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
