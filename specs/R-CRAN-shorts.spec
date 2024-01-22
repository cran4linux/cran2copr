%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shorts
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Short Sprints

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-LambertW 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-LambertW 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-purrr 

%description
Create short sprint acceleration-velocity (AVP) and force-velocity (FVP)
profiles and predict kinematic and kinetic variables using the timing-gate
split times, laser or radar gun data, tether devices data, as well as the
data provided by the GPS and LPS monitoring systems. The modeling method
utilized in this package is based on the works of Furusawa K, Hill AV,
Parkinson JL (1927) <doi: 10.1098/rspb.1927.0035>, Greene PR. (1986) <doi:
10.1016/0025-5564(86)90063-5>, Chelly SM, Denis C. (2001) <doi:
10.1097/00005768-200102000-00024>, Clark KP, Rieger RH, Bruno RF, Stearne
DJ. (2017) <doi: 10.1519/JSC.0000000000002081>, Samozino P. (2018) <doi:
10.1007/978-3-319-05633-3_11>, Samozino P. and Peyrot N., et al (2022)
<doi: 10.1111/sms.14097>, Clavel, P., et al (2023) <doi:
10.1016/j.jbiomech.2023.111602>, and Jovanovic M. (2023) <doi:
10.1080/10255842.2023.2170713>.

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
