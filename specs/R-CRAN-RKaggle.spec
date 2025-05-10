%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RKaggle
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          'Kaggle' Dataset Downloader 'API'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-readODS 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-readODS 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-sf 

%description
Easily download datasets from Kaggle <https://www.kaggle.com/> directly
into your R environment using 'RKaggle'. Streamline your data analysis
workflows by importing datasets effortlessly and focusing on insights
rather than manual data handling. Perfect for data enthusiasts and
professionals looking to integrate Kaggle datasets into their R projects
with minimal hassle.

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
