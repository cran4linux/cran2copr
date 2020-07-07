%global packname  googleLanguageR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Call Google's 'Natural Language' API, 'Cloud Translation' API,'Cloud Speech' API and 'Cloud Text-to-Speech' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-googleAuthR >= 1.1.1
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-googleAuthR >= 1.1.1
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Call 'Google Cloud' machine learning APIs for text and speech tasks. Call
the 'Cloud Translation' API <https://cloud.google.com/translate/> for
detection and translation of text, the 'Natural Language' API
<https://cloud.google.com/natural-language/> to analyse text for
sentiment, entities or syntax, the 'Cloud Speech' API
<https://cloud.google.com/speech/> to transcribe sound files to text and
the 'Cloud Text-to-Speech' API <https://cloud.google.com/text-to-speech/>
to turn text into sound files.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/OSR_us_000_0010_8k.wav
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/woman1_wb.wav
%{rlibdir}/%{packname}/INDEX
