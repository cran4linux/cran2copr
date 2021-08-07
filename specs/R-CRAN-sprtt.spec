%global __brp_check_rpaths %{nil}
%global packname  sprtt
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Probability Ratio Tests: Using t-Statistic

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-stats 

%description
The seq_ttest() function is the implementation of Abraham Wald’s (1947)
<doi:10.2134/agronj1947.00021962003900070011x> Sequential Probability
Ratio Test (SPRT) for the test of a normal mean (difference) with unknown
variance in R (R Core Team, 2018). It performs sequential t tests
developed by Rushton (1950) <doi:10.2307/2332385>, Rushton (1952)
<doi:10.2307/2334026> and Hajnal (1961) <doi:10.2307/2333131>, based on
the SPRT. Specifically, seq_ttest() performs one-sample, two-sample, and
paired t tests for testing one- and two-sided hypotheses.  The test is to
be applied to the data during the sampling process, ideally after each
observation. At any stage, it will return a decision to either continue
sampling or terminate and accept one of the specified hypotheses. For more
information on the SPRT t test, see Schnuerch & Erdfelder (2019)
<doi:10.1037/met0000234>.

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
