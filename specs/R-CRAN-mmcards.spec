%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mmcards
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Playing Cards Utility Functions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Early insights in probability theory were largely influenced by questions
about gambling and games of chance, as noted by Blitzstein and Hwang
(2019, ISBN:978-1138369917). In modern times, playing cards continue to
serve as an effective teaching tool for probability, statistics, and even
'R' programming, as demonstrated by Grolemund (2014, ISBN:978-1449359010).
The 'mmcards' package offers a collection of utility functions designed to
aid in the creation, manipulation, and utilization of playing card decks
in multiple formats. These include a standard 52-card deck, as well as
alternative decks such as decks defined by custom anonymous functions and
custom interleaved decks. Optimized for the development of educational
'shiny' applications, the package is particularly useful for teaching
statistics and probability through card-based games. Functions include
shuffle_deck(), which creates either a shuffled standard deck or a
shuffled custom alternative deck; deal_card(), which takes a deck and
returns a list object containing both the dealt card and the updated deck;
and i_deck(), which adds image paths to card objects, further enriching
the package's utility in the development of interactive 'shiny'
application card games.

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
