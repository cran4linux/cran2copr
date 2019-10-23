%global packname  tabr
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Music Notation Syntax, Manipulation, Analysis and Transcriptionin R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         lilypond
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggplot2 

%description
Provides a music notation syntax and a collection of music programming
functions for generating, manipulating, organizing and analyzing musical
information in R. The music notation framework facilitates creating and
analyzing music data in notation form. The package also provides API
wrapper functions for transcribing musical representations in R into
guitar tablature ("tabs") using the 'LilyPond' backend
(<http://lilypond.org>). 'LilyPond' is open source music engraving
software for generating high quality sheet music based on markup syntax.
'tabr' generates 'LilyPond' files from R code and can pass them to
'LilyPond' to be rendered into sheet music pdf files from R. While
'LilyPond' caters to sheet music in general and 'tabr' can be used to
create basic sheet music, the transcription functions focus on leveraging
'LilyPond' specifically for creating quality guitar tablature. The package
offers nominal MIDI file output support in conjunction with rendering
tablature output. See the 'tuneR' package for more general use of MIDI
files in R.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example.mid
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
