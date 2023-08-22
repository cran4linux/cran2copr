%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bootwar
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Bootstrap Test with Pooled Resampling Card Game

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-npboottprm 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinythemes 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-npboottprm 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinythemes 

%description
The card game War is simple in its rules but can be lengthy. In another
domain, the nonparametric bootstrap test with pooled resampling (nbpr)
methods, as outlined in Dwivedi, Mallawaarachchi, and Alvarado (2017)
<doi:10.1002/sim.7263>, is optimal for comparing paired or unpaired means
in non-normal data, especially for small sample size studies. However,
many researchers are unfamiliar with these methods. The 'bootwar' package
bridges this gap by enabling users to grasp the concepts of nbpr via Boot
War, a variation of the card game War designed for small samples. With the
shuffle_cards() function, players can engage in Boot War using a standard
52-card deck, a custom deck created via an anonymous function, or
interleaved custom decks where each player has their distinct deck. The
package further provides functions like deal_card(), score_keeper(), and
play_round() to streamline gameplay and scoring. Once a predetermined
number of rounds concludes, users can employ the analyze_game() function
to derive game results. This function leverages the 'npboottprm' package's
nonparboot() to report nbpr results and, for comparative analysis, also
reports results from the 'stats' package's t.test() function.
Additionally, 'bootwar' features an interactive 'shiny' web application,
bootwar(). This offers a user-centric interface to experience Boot War,
enhancing understanding of nbpr methods across various distributions,
sample sizes, number of bootstrap resamples, and confidence intervals.

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
