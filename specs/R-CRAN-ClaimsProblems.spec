%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ClaimsProblems
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Conflicting Claims

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rgl 

%description
The analysis of conflicting claims arises when an amount has to be divided
among a set of agents with claims that exceed what is available. A rule is
a way of selecting a division among the claimants. This package computes
the main rules introduced in the literature from ancient times to the
present. The inventory of rules covers the proportional and the adjusted
proportional rules, the constrained equal awards and the constrained equal
losses rules, the constrained egalitarian, the Piniles’ and the minimal
overlap rules, the random arrival and the Talmud rules. Besides, the
Dominguez and Thomson and the average-of-awards rules are also included.
All of them can be found in the book by W. Thomson (2019), How to divide
when there isn't enough. From Aristotle, the Talmud, and Maimonides to the
axiomatics of resource allocation', except for the average-of-awards rule,
introduced by Mirás Calvo et al. (2022), <doi:10.1007/s00355-022-01414-6>.
In addition, graphical diagrams allow the user to represent, among others,
the set of awards, the paths of awards, the schedules of awards of a rule,
and some indexes. A good understanding of the similarities and differences
between the rules is useful for better decision-making. Therefore, this
package could be helpful to students, researchers, and managers alike.
For a more detailed explanation of the package, see Mirás Calvo et al.
(2023), <doi:10.1016/j.dajour.2022.100160>.

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
