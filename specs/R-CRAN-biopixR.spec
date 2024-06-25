%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  biopixR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extracting Insights from Biological Images

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-cluster 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-magick 
Requires:         R-tcltk 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-cluster 

%description
Combines the 'magick' and 'imager' packages to streamline image analysis,
focusing on feature extraction and quantification from biological images,
especially microparticles. By providing high throughput pipelines and
clustering capabilities, 'biopixR' facilitates efficient insight
generation for researchers (Schneider J. et al. (2019)
<doi:10.21037/jlpm.2019.04.05>).

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
