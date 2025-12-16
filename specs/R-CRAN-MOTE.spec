%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MOTE
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Effect Size and Confidence Interval Calculator

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Measure of the Effect ('MOTE') is an effect size calculator, including a
wide variety of effect sizes in the mean differences family (all versions
of d) and the variance overlap family (eta, omega, epsilon, r). 'MOTE'
provides non-central confidence intervals for each effect size, relevant
test statistics, and output for reporting in APA Style (American
Psychological Association, 2010, <ISBN:1433805618>) with 'LaTeX'. In
research, an over-reliance on p-values may conceal the fact that a study
is under-powered (Halsey, Curran-Everett, Vowler, & Drummond, 2015
<doi:10.1038/nmeth.3288>). A test may be statistically significant, yet
practically inconsequential (Fritz, Scherndl, & Kühberger, 2012
<doi:10.1177/0959354312436870>). Although the American Psychological
Association has long advocated for the inclusion of effect sizes
(Wilkinson & American Psychological Association Task Force on Statistical
Inference, 1999 <doi:10.1037/0003-066X.54.8.594>), the vast majority of
peer-reviewed, published academic studies stop short of reporting effect
sizes and confidence intervals (Cumming, 2013,
<doi:10.1177/0956797613504966>). 'MOTE' simplifies the use and
interpretation of effect sizes and confidence intervals.

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
