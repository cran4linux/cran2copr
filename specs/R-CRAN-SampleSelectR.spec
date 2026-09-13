%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SampleSelectR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Randomly Select Samples for Various Probability-Based Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidytable 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidytable 
Requires:         R-utils 

%description
Randomly select samples using simple random sampling (SRS), systematic
sampling, and various probability proportional to size (PPS) methods,
including systematic PPS and sequential PPS (i.e., Chromy's method). Also
includes functionality to allocate sample sizes across strata using
proportional, power, Neyman, and optimal allocation methods, and to select
samples within strata. Designed to make survey sample design and selection
reproducible, efficient, and transparent for survey statisticians and
researchers. Sampling methods follow Kalton (1983)
<doi:10.4135/9781412984683> and Chromy (1979)
<http://www.asasrms.org/Proceedings/papers/1979_081.pdf>.

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
