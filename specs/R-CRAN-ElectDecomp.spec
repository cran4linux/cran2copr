%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ElectDecomp
%global packver   0.0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Decomposition of Seats-to-Votes Distortion in Multimember Elections

License:          EPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Decomposes the seat-to-vote distortion for every party (individual party
bias or individual party deviation from proportional representation) into
segments that can be attributed to separate causes for the party infra or
over-representation: the electoral system effect (separating the mean and
the variance effect within it) and the population effect (separating
malapportionment and unequal participation effect within it).  It works on
(single tired) districted electoral systems with any number of seats per
district. In addition, the package aggregates the individual party
distortion into an index of deviation from proportionality (the
Losemore-Hanby index) whose value is also decomposed into segments
attributed to the major causes of deviation from proportionality (plus the
interactions among them).

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
