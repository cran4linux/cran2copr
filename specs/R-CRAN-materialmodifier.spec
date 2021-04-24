%global packname  materialmodifier
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Apply Material Editing Effects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-readbitmap 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-downloader 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-moments 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-png 
Requires:         R-CRAN-readbitmap 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-downloader 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-moments 

%description
You can apply image processing effects that modifies the perceived
material properties such as gloss, smoothness, and blemishes. This is an
implementation of the algorithm proposed by Boyadzhiev et al. (2015)
"Band-Sifting Decomposition for Image Based Material Editing".
Documentation and practical tips of the package is available at
<https://github.com/tsuda16k/materialmodifier>.

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
