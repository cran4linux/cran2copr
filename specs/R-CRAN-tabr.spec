%global __brp_check_rpaths %{nil}
%global packname  tabr
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Music Notation Syntax, Manipulation, Analysis and Transcription in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         lilypond
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggplot2 

%description
Provides a music notation syntax and a collection of music programming
functions for generating, manipulating, organizing and analyzing musical
information in R. The music notation framework facilitates creating and
analyzing music data in notation form. Music data can be viewed,
manipulated and analyzed while in different forms of representation based
around different data structures: strings and data frames. Each
representation offers advantages over the other for different use cases.
Music syntax can be entered directly and represented in character strings
to minimize the formatting overhead of data entry by using simple data
structures, for example when wanting to quickly enter and transcribe short
pieces of music to sheet music or tablature. The package contains
functions for directly performing various mathematical, logical and
organizational operations and musical transformations on special object
classes that facilitate working with music data and notation. The same
music data can also be organized in tidy data frames, allowing for a more
familiar and powerful approach to the analysis of large amounts of
structured music data. Functions are available for mapping seamlessly
between these data structures and their representations of musical
information. The package also provides API wrapper functions for
transcribing musical representations in R into guitar tablature ("tabs")
and basic sheet music using the 'LilyPond' backend
(<http://lilypond.org>). 'LilyPond' is open source music engraving
software for generating high quality sheet music based on markup syntax.
The package generates 'LilyPond' files from R code and can pass them to
'LilyPond' to be rendered into sheet music pdf files. The package offers
nominal MIDI file output support in conjunction with rendering sheet
music. The package can read MIDI files and attempts to structure the MIDI
data to integrate as best as possible with the data structures and
functionality found throughout the package.

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
