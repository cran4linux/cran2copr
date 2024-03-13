%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rgeoboundaries
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          geoBoundaries Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-crul >= 1.4.0
BuildRequires:    R-CRAN-countrycode >= 1.2.0
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-hoardr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-crul >= 1.4.0
Requires:         R-CRAN-countrycode >= 1.2.0
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-hoardr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-lifecycle 

%description
Provides access to the geoBoundaries international boundary database
<https://www.geoboundaries.org>, a NSF and foundation supported dataset of
subnational boundaries around the globe.  Methods allow you to access data
directly from the API <https://www.geoboundaries.org/api/current/> to
query for the geometric boundaries for any country, globally. For more
details, refer to the publication by Runfola et al. (2020)
<doi:10.1371/journal.pone.0231866>.

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
