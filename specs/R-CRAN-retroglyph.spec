%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  retroglyph
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          A Trusted Mini-Agent to Reconstruct Individual Patient Data from Kaplan-Meier Images

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinychat >= 0.5.0
BuildRequires:    R-CRAN-ellmer >= 0.4.1
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-diffviewer 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-IPDfromKM 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tesseract 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-shinychat >= 0.5.0
Requires:         R-CRAN-ellmer >= 0.4.1
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-diffviewer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-IPDfromKM 
Requires:         R-CRAN-later 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tesseract 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 

%description
The enclosed agent reconstructs individual patient data from published
Kaplan-Meier curve images. Relative to other Kaplan-Meier reconstruction
tools, it excels at untangling egregiously occluded Kaplan-Meier curves,
and the digitization phase achieves a high level of pixel precision.

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
