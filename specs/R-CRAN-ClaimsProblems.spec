%global __brp_check_rpaths %{nil}
%global packname  ClaimsProblems
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Conflicting Claims

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
Requires:         R-graphics 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-geometry 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-pracma 

%description
The analysis of conflicting claims arises when an amount has to be divided
among a set of agents with claims that exceed what is available. A rule is
a way of selecting a division among the claimants. This package computes
the main rules introduced in the literature from the old times until
nowadays. The inventory of rules covers the proportional and the adjusted
proportional rules, the constrained equal awards and the constrained equal
losses rules, the constrained egalitarian, the Piniles’ and the minimal
overlap rules, the random arrival and the Talmud rules. Besides, the
Dominguez and Thomson and the average of awards rules are also included.
All of them can be found in the book of W. Thomson (2019), 'How to divide
when there isn't enough. From Aristotle, the Talmud, and Maimonides to the
axiomatics of resource allocation', with the exception of the average of
awards rule (Mirás Calvo et al. (2022), <doi:10.1007/s00355-022-01414-6>).
In addition, graphical diagrams allow the user to represent, among others,
the set of awards, the paths of awards, and the schedules of awards of a
rule, and some indexes. A good understanding of the similarities and the
differences of the rules is useful for a better decision making. Therefore
this package could be helpful to students, researchers and managers alike.

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
