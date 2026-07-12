%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TheOrdinals
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Aggregation and Consensus Methods for Preference-Approvals

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ConsRank 
Requires:         R-CRAN-ConsRank 

%description
Tools for aggregating ordinal preference data into a group consensus. The
package implements DIVA (Divide and Conquer for Preference-Approvals), a
distance-based aggregation method for preference-approvals, that is,
preference data in which voters express both a (weak) ranking and an
approval of the alternatives. The consensus is the preference-approval
minimising the average distance to the set of voters, measured through the
family of distances of Erdamar, Garcia-Lapresta, Perez-Roman and Sanver
(2014) <doi:10.1016/j.mathsocsci.2013.10.005>. Methods and applications
are described in Albano and Romano (2026)
<doi:10.1007/s11634-025-00663-4>. The package is designed to be extended
with further methods for ordinal preference data.

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
