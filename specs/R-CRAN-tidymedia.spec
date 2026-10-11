%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidymedia
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Media File Preprocessing and Metadata for the 'tidyverse'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.1.4
BuildRequires:    R-CRAN-withr >= 2.5.0
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-rlang >= 1.2.0
BuildRequires:    R-CRAN-archive >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-digest >= 0.6.37
BuildRequires:    R-CRAN-rappdirs >= 0.3.3
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-tibble >= 3.1.4
Requires:         R-CRAN-withr >= 2.5.0
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-rlang >= 1.2.0
Requires:         R-CRAN-archive >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-digest >= 0.6.37
Requires:         R-CRAN-rappdirs >= 0.3.3
Requires:         R-tools 
Requires:         R-utils 

%description
Batch preprocessing and metadata extraction for audio, video and image
files, built on the command-line programs 'FFmpeg' (<https://ffmpeg.org/>)
and 'MediaInfo' (<https://mediaarea.net/en/MediaInfo>). Trim, crop, scale,
convert and standardize files one at a time or across a whole directory,
and read container and stream metadata back as tibbles for use with the
'tidyverse'.

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
