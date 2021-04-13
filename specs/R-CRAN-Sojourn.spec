%global packname  Sojourn
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Apply Sojourn Methods for Processing ActiGraph Accelerometer Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet >= 7.3
BuildRequires:    R-CRAN-zoo >= 1.8
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-svDialogs >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-PAutilities >= 0.2.0
BuildRequires:    R-CRAN-rlang >= 0.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-nnet >= 7.3
Requires:         R-CRAN-zoo >= 1.8
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-svDialogs >= 1.0
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-PAutilities >= 0.2.0
Requires:         R-CRAN-rlang >= 0.2
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
Provides a simple way for utilizing Sojourn methods for accelerometer
processing, as detailed in Lyden K, Keadle S, Staudenmayer J, & Freedson P
(2014) <doi:10.1249/MSS.0b013e3182a42a2d>, Ellingson LD, Schwabacher IJ,
Kim Y, Welk GJ, & Cook DB (2016) <doi:10.1249/MSS.0000000000000915>, and
Hibbing PR, Ellingson LD, Dixon PM, & Welk GJ (2018)
<doi:10.1249/MSS.0000000000001486>. The accompanying Sojourn.Data package,
if not available on CRAN, can be accessed from
<https://github.com/paulhibbing/Sojourn.Data>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
