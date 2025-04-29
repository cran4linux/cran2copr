%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tabr
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Music Notation Syntax, Manipulation, Analysis and Transcription in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       lilypond
BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Provides a music notation syntax and a collection of music programming
functions for generating, manipulating, organizing, and analyzing musical
information in R. Music syntax can be entered directly in character
strings, for example to quickly transcribe short pieces of music. The
package contains functions for directly performing various mathematical,
logical and organizational operations and musical transformations on
special object classes that facilitate working with music data and
notation. The same music data can be organized in tidy data frames for a
familiar and powerful approach to the analysis of large amounts of
structured music data. Functions are available for mapping seamlessly
between these formats and their representations of musical information.
The package also provides an API to 'LilyPond' (<https://lilypond.org/>)
for transcribing musical representations in R into tablature ("tabs") and
sheet music. 'LilyPond' is open source music engraving software for
generating high quality sheet music based on markup syntax. The package
generates 'LilyPond' files from R code and can pass them to the 'LilyPond'
command line interface to be rendered into sheet music PDF files or
inserted into R markdown documents. The package offers nominal MIDI file
output support in conjunction with rendering sheet music. The package can
read MIDI files and attempts to structure the MIDI data to integrate as
best as possible with the data structures and functionality found
throughout the package.

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
