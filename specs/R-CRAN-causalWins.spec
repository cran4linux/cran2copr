%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  causalWins
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compute the Causal Win Ratio Using Nearest Neighbor Matching

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-drf 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-grf 
BuildRequires:    R-CRAN-MatchIt 
Requires:         R-CRAN-drf 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-grf 
Requires:         R-CRAN-MatchIt 

%description
Based on “Rethinking the Win Ratio: A Causal Framework for Hierarchical
Outcome Analysis” (M. Even and J. Josse, 2025), this package provides
implementations of three approaches - nearest neighbor matching,
distributional regression forests, and efficient influence functions - to
estimate the causal win ratio, win proportion, and net benefit.

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
