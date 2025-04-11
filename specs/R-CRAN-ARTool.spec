%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ARTool
%global packver   0.11.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.2
Release:          1%{?dist}%{?buildtag}
Summary:          Aligned Rank Transform

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-car >= 2.0.24
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emmeans 
Requires:         R-CRAN-car >= 2.0.24
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emmeans 

%description
The aligned rank transform for nonparametric factorial ANOVAs as described
by Wobbrock, Findlater, Gergle, and Higgins (2011)
<doi:10.1145/1978942.1978963>. Also supports aligned rank transform
contrasts as described by Elkin, Kay, Higgins, and Wobbrock (2021)
<doi:10.1145/3472749.3474784>.

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
