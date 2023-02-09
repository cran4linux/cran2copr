%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CoronaNetR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          API Access to 'CoronaNet' Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-readr 

%description
Offers access to a database on government responses to the COVID-19
pandemic. To date, the 'CoronaNet' dataset provides the most comprehensive
and granular documentation of such government policies in the world,
capturing data for 20 broad policy categories alongside many other
dimensions, including the initiator, target, and timing of a policy. This
package is a programmatic front-end to up-to-date 'CoronaNet' policy
records and the 'CoronaNet' policy intensity index scores. For more
information, see Cheng et al. (2020) <doi:10.1038/s41562-020-0909-7>.

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
