%global __brp_check_rpaths %{nil}
%global packname  VEwaning
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Vaccine Efficacy Over Time

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 

%description
Implements methods for inference on potential waning of vaccine efficacy
and for estimation of vaccine efficacy at a user-specified time after
vaccination based on data from a randomized, double-blind,
placebo-controlled vaccine trial in which participants may be unblinded
and placebo subjects may be crossed over to the study vaccine.  The
methods also allow adjustment for possible confounding via inverse
probability weighting through specification of models for the trial entry
process, unblinding mechanisms, and the probability an unblinded placebo
participant accepts study vaccine: Tsiatis, A. A. and Davidian, M. (2021)
<arXiv:2102.13103> .

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
