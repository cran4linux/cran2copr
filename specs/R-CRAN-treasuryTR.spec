%global packname  treasuryTR
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Treasury Total Returns from Yield Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xts >= 0.9.0
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-xts >= 0.9.0
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 

%description
Generate Total Returns (TR) from bond yield data with fixed maturity, e.g.
reported treasury yields. The generated TR series are very close to
alternative series that can be purchased (e.g. CRSP, Bloomberg),
suggesting they are a high-quality alternative for those, see Swinkels
(2019) <doi:10.3390/data4030091>.

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
