%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dataset
%global packver   0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          Create Data Frames that are Easier to Exchange and Reuse

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-ISOcodes 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-ISOcodes 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 

%description
The aim of the 'dataset' package is to make tidy datasets easier to
release, exchange and reuse. It organizes and formats data frame 'R'
objects into well-referenced, well-described, interoperable datasets into
release and reuse ready form.

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
