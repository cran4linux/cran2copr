%global packname  autoFC
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Construction of Forced-Choice Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-irrCAC 
Requires:         R-CRAN-irrCAC 

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
construction of FC tests, essentially exempting users from the burden of
manual item pairing and reducing the computational costs and biases
induced by simple ranking methods. Given characteristics of each item (and
item responses), FC tests can be automatically constructed based on
user-defined pairing criteria and weights as well as customized
optimization behavior. Users can also construct parallel forms of the same
test following the same pairing rules.

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
