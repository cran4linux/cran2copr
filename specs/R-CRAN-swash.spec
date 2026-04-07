%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  swash
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Health Geography Toolbox for Model-Based Analysis of Infections Panel Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-methods 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-strucchange 
Requires:         R-methods 

%description
Within epidemic outbreaks, infections grow and decline differently between
regions, and the velocity of spatial spread differs between countries. The
swash library offers a set of model-based analyses for these topics.
Spread velocity may be analysed with the Swash-Backwash Model for the
Single Epidemic Wave and corresponding functions for bootstrap confidence
intervals, country comparison, and visualization of results. Differences
in epidemic growth between regions may be analysed using logistic growth
models, exponential growth models, Hawkes processes and breakpoint
analyses. All functionalities are accessed by the class "infpan" for
infections panel data defined in this package, which is built from a
data.frame provided by the user.

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
