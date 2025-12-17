%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  biostats
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Biostatistics and Clinical Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-nortest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-car 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-nortest 

%description
Biostatistical and clinical data analysis, including descriptive
statistics, exploratory data analysis, sample size and power calculations,
statistical inference, and data visualization. Normality tests are
implemented following Mishra et al. (2019) <doi:10.4103/aca.ACA_157_18>,
omnibus test procedures are based on Blanca et al. (2017)
<doi:10.3758/s13428-017-0918-2> and Field et al. (2012,
ISBN:9781446200469), while sample size and power calculation methods
follow Chow et al. (2017) <doi:10.1201/9781315183084>.

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
