%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  socialranking
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Social Ranking Solutions for Power Relations on Coalitions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 2.4
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-relations >= 0.6.13
Requires:         R-CRAN-Rdpack >= 2.4
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-relations >= 0.6.13

%description
The notion of power index has been widely used in literature to evaluate
the influence of individual players (e.g., voters, political parties,
nations, stockholders, etc.) involved in a collective decision situation
like an electoral system, a parliament, a council, a management board,
etc., where players may form coalitions. Traditionally this ranking is
determined through numerical evaluation. More often than not however only
ordinal data between coalitions is known. The package 'socialranking'
offers a set of solutions to rank players based on a transitive ranking
between coalitions, including through CP-Majority, ordinal Banzhaf or
lexicographic excellence solution summarized by Tahar Allouche, Bruno
Escoffier, Stefano Moretti and Meltem Öztürk (2020,
<doi:10.24963/ijcai.2020/3>).

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
