%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  horizonclaims
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Claims About the Risk at a Fixed Time from Censored Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Rules for demonstrating that the cumulative incidence of an event at a
fixed time lies below a threshold, from right-censored follow-up data. The
package gives the one-sided upper confidence limit of the beta product
confidence procedure of Fay, Brittain and Proschan (2013)
<doi:10.1093/biostatistics/kxt016> and of its mid-p version of Fay and
Brittain (2016) <doi:10.1002/sim.6905>, the Kaplan-Meier estimate with the
log-log limit and the number at risk, and exact binomial limits for
patients whose potential follow-up reaches the fixed time, including a
limit that counts patients lost to follow-up as having had the event. It
also gives the smallest number of patients at risk with which a claim can
be demonstrated, the number of patients needed for a given power, and a
lower confidence bound for the time during which the risk stays below a
threshold, obtained by testing prespecified times in a fixed order.

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
