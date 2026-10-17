%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  actiplot
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plotting Minute-Level Activity Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-actibase >= 0.6.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-actibase >= 0.6.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-rlang 

%description
Provides 'ggplot2' plots for minute-level activity data, including step
counts and activity counts. Time series can be displayed over the full
recording period or aligned by time of day and faceted into one row per
date.  Includes example activity data described by Chadwell et al. (2019)
<doi:10.1038/s41597-019-0211-6>.

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
