%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evenBreak
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Posteriori Probs of Suits Breaking Evenly Across Four Hands

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-combinat 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
We quantitatively evaluated the assertion that says if one suit is found
to be evenly distributed among the 4 players, the rest of the suits are
more likely to be evenly distributed. Our mathematical analyses show that,
if one suit is found to be evenly distributed, then a second suit has a
slightly elevated probability (ranging between 10%% to 15%%) of being evenly
distributed. If two suits are found to be evenly distributed, then a third
suit has a substantially elevated probability (ranging between 30%% to 50%%)
of being evenly distributed.This package refers to methods and authentic
data from Ely Culbertson <https://www.bridgebum.com/law_of_symmetry.php>,
Gregory Stoll <https://gregstoll.com/~gregstoll/bridge/math.html>, and
details of performing the probability calculations from Jeremy L. Martin
<https://jlmartin.ku.edu/~jlmartin/bridge/basics.pdf>, Emile Borel and
Andre Cheron (1954) "The Mathematical Theory of Bridge",Antonio Vivaldi
and Gianni Barracho (2001, ISBN:0 7134 8663 5) "Probabilities and
Alternatives in Bridge", Ken Monzingo (2005) "Hand and Suit Patterns"
<http://web2.acbl.org/documentlibrary/teachers/celebritylessons/handpatternsrevised.pdf>Ken
Monzingo (2005) "Hand and Suit Patterns"
<http://web2.acbl.org/documentlibrary/teachers/celebritylessons/handpatternsrevised.pdf>.

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
