%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyEmoji
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Discover, Count and Score Emoji in Text

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-emoji 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-emoji 
Requires:         R-CRAN-lifecycle 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
A tidy toolkit for working with the emoji in any text column, such as
social-media posts, product reviews, chat logs or survey responses.
Unicode is awkward to handle and not every code point is an emoji, which
makes emoji statistics fiddly to obtain. 'tidyEmoji' extracts, counts,
categorises and sentiment-scores emoji with grapheme-aware detection (so
skin-tone and multi-person sequences stay intact), returning tidy data
frames that slot straight into a 'tidyverse' workflow. The bundled emoji
sentiment lexicon is from the Emoji Sentiment Ranking of Kralj Novak et
al. (2015) <doi:10.1371/journal.pone.0144296>, released under CC BY-SA
4.0.

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
