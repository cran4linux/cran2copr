%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  globaltrends
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Download and Measure Global Trends Through 'Google' Search Volumes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-gtrendsR >= 1.5.1
BuildRequires:    R-CRAN-reticulate >= 1.38
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-utils 
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-gtrendsR >= 1.5.1
Requires:         R-CRAN-reticulate >= 1.38
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-utils 

%description
'Google' offers public access to global search volumes from its search
engine through the 'Google Trends' portal. The package downloads these
search volumes provided by 'Google Trends' and uses them to measure and
analyze the distribution of search scores across countries or within
countries. The package allows researchers and analysts to use these search
scores to investigate global trends based on patterns within these scores.
This offers insights such as degree of internationalization of firms and
organizations or dissemination of political, social, or technological
trends across the globe or within single countries.  An outline of the
package's methodological foundations and potential applications is
available as a working paper: <doi:10.2139/ssrn.3969013>.

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
