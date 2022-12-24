%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BetaBit
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mini Games from Adventures of Beta and Bit

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-digest 

%description
Three games: proton, frequon and regression. Each one is a console-based
data-crunching game for younger and older data scientists. Act as a
data-hacker and find Slawomir Pietraszko's credentials to the Proton
server. In proton you have to solve four data-based puzzles to find the
login and password. There are many ways to solve these puzzles. You may
use loops, data filtering, ordering, aggregation or other tools. Only
basics knowledge of R is required to play the game, yet the more functions
you know, the more approaches you can try. In frequon you will help to
perform statistical cryptanalytic attack on a corpus of ciphered messages.
This time seven sub-tasks are pushing the bar much higher. Do you accept
the challenge? In regression you will test your modeling skills in a
series of eight sub-tasks. Try only if ANOVA is your close friend. It's a
part of Beta and Bit project. You will find more about the Beta and Bit
project at <https://github.com/BetaAndBit/Wykresy>.

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
