%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  walkboutr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Walk Bouts from GPS and Accelerometry Data

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-measurements 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-lwgeom 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-measurements 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Process GPS and accelerometry data to generate walk bouts. A walk bout is
a period of activity with accelerometer movement matching the patterns of
walking with corresponding GPS measurements that confirm travel. The
inputs of the 'walkboutr' package are individual-level accelerometry and
GPS data. The outputs of the model are walk bouts with corresponding
times, duration, and summary statistics on the sample population, which
collapse all personally identifying information. These bouts can be used
to measure walking both as an outcome of a change to the built environment
or as a predictor of health outcomes such as a cardioprotective behavior.
Kang B, Moudon AV, Hurvitz PM, Saelens BE (2017)
<doi:10.1016/j.trd.2017.09.026>.

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
