%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  transforEmotion
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Transformer Emotion Analysis for Text, Image, Video, and Speech

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httpuv >= 1.6.0
BuildRequires:    R-CRAN-reticulate >= 1.45.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-textdata 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-httpuv >= 1.6.0
Requires:         R-CRAN-reticulate >= 1.45.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-googledrive 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-textdata 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-httr 

%description
Zero-shot emotion classification for text, images, video and speech, and
tools to find faces and code them by hand. Text is scored with 'Hugging
Face' transformer pipelines (default
'cross-encoder/nli-distilroberta-base'). Images and video are scored with
'OpenAI CLIP'; faces can be limited to those found by 'OpenCV YuNet'.
Speech segments are scored with 'LAION CLAP'. Frame scores can be
calibrated and combined into posteriors, and detected faces or other items
can be turned into a local coding task served from R. Any other zero-shot
model can be selected by its name on <https://huggingface.co/models>. For
details see Tomašević, Golino, and Christensen (2026)
<doi:10.5117/CCR2026.2.2.TOMA>.

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
