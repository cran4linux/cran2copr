%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  text2speech
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Text to Speech Conversion

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-aws.signature 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-googleAuthR 
BuildRequires:    R-CRAN-googleLanguageR 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-conrad 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-aws.signature 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-googleAuthR 
Requires:         R-CRAN-googleLanguageR 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-conrad 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tuneR 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Converts text into speech using various text-to-speech (TTS) engines and
provides an unified interface for accessing their functionality. With this
package, users can easily generate audio files of spoken words, phrases,
or sentences from plain text data. The package supports multiple TTS
engines, including Google's 'Cloud Text-to-Speech API', 'Amazon Polly',
Microsoft's 'Cognitive Services Text to Speech REST API', the 'Speechify
Text-to-Speech API', and a free TTS engine called 'Coqui TTS'.

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
