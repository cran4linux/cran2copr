%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PytrendsLongitudinalR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Create Longitudinal Google Trends Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-utils 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-reticulate 
Requires:         R-utils 

%description
'Google Trends' provides cross-sectional and time-series data on searches,
but lacks readily available longitudinal data. Researchers, who want to
create longitudinal 'Google Trends' on their own, face practical
challenges, such as normalized counts that make it difficult to combine
cross-sectional and time-series data and limitations in data formats and
timelines that limit data granularity over extended time periods. This
package addresses these issues and enables researchers to generate
longitudinal 'Google Trends' data. This package is built on 'pytrends', a
Python library that acts as the unofficial 'Google Trends API' to collect
'Google Trends' data. As long as the 'Google Trends API', 'pytrends' and
all their dependencies are working, this package will work. During
testing, we noticed that for the same input (keyword, topic, data_format,
timeline), the output index can vary from time to time. Besides, if the
keyword is not very popular, then the resulting dataset will contain a lot
of zeros, which will greatly affect the final result. While this package
has no control over the accuracy or quality of 'Google Trends' data, once
the data is created, this package coverts it to longitudinal data. In
addition, the user may encounter a 429 Too Many Requests error when using
cross_section() and time_series() to collect 'Google Trends' data. This
error indicates that the user has exceeded the rate limits set by the
'Google Trends API'. For more information about the 'Google Trends API' -
'pytrends', visit <https://pypi.org/project/pytrends/>.

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
