%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autoFC
%global packver   0.2.0.1002
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0.1002
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Construction of Forced-Choice Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-irrCAC 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-SimDesign 
BuildRequires:    R-CRAN-thurstonianIRT 
BuildRequires:    R-CRAN-MplusAutomation 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-irrCAC 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-SimDesign 
Requires:         R-CRAN-thurstonianIRT 
Requires:         R-CRAN-MplusAutomation 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-tidyr 

%description
Forced-choice (FC) response has gained increasing popularity and interest
for its resistance to faking when well-designed (Cao & Drasgow, 2019
<doi:10.1037/apl0000414>). To established well-designed FC scales,
typically each item within a block should measure different trait and have
similar level of social desirability (Zhang et al., 2020
<doi:10.1177/1094428119836486>). Recent study also suggests the importance
of high inter-item agreement of social desirability between items within a
block (Pavlov et al., 2021 <doi:10.31234/osf.io/hmnrc>). In addition to
this, FC developers may also need to maximize factor loading differences
(Brown & Maydeu-Olivares, 2011 <doi:10.1177/0013164410375112>) or minimize
item location differences (Cao & Drasgow, 2019 <doi:10.1037/apl0000414>)
depending on scoring models. Decision of which items should be assigned to
the same block, termed item pairing, is thus critical to the quality of an
FC test. This pairing process is essentially an optimization process which
is currently carried out manually. However, given that we often need to
simultaneously meet multiple objectives, manual pairing becomes
impractical or even not feasible once the number of latent traits and/or
number of items per trait are relatively large. To address these problems,
autoFC is developed as a practical tool for facilitating the automatic
construction of FC tests (Li et al., 2022
<doi:10.1177/01466216211051726>), essentially exempting users from the
burden of manual item pairing and reducing the computational costs and
biases induced by simple ranking methods. Given characteristics of each
item (and item responses), FC measures can be constructed either
automatically based on user-defined pairing criteria and weights, or based
on exact specifications of each block (i.e., blueprint; see Li et al.,
2024 <doi:10.1177/10944281241229784>). Users can also generate simulated
responses based on the Thurstonian Item Response Theory model (Brown &
Maydeu-Olivares, 2011 <doi:10.1177/0013164410375112>) and predict trait
scores of simulated/actual respondents based on an estimated model.

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
