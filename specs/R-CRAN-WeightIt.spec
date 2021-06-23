%global __brp_check_rpaths %{nil}
%global packname  WeightIt
%global packver   0.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.0
Release:          1%{?dist}%{?buildtag}
Summary:          Weighting for Covariate Balance in Observational Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cobalt >= 4.3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-backports >= 1.2.0
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-cobalt >= 4.3.0
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-backports >= 1.2.0
Requires:         R-CRAN-crayon 

%description
Generates weights to form equivalent groups in observational studies with
point or longitudinal treatments by easing and extending the functionality
of the R packages 'twang' for generalized boosted modeling (McCaffrey,
Ridgeway & Morral, 2004) <doi:10.1037/1082-989X.9.4.403>, 'CBPS' for
covariate balancing propensity score weighting (Imai & Ratkovic, 2014)
<doi:10.1111/rssb.12027>, 'ebal' for entropy balancing (Hainmueller, 2012)
<doi:10.1093/pan/mpr025>, 'optweight' for optimization-based weights
(Zubizarreta, 2015) <doi:10.1080/01621459.2015.1023805>, 'ATE' for
empirical balancing calibration weighting (Chan, Yam, & Zhang, 2016)
<doi:10.1111/rssb.12129>, 'SuperLearner' for stacked machine
learning-based propensity scores (Pirracchio, Petersen, & van der Laan,
2015) <doi:10.1093/aje/kwu253>, among others. Also allows for assessment
of weights and checking of covariate balance by interfacing directly with
'cobalt'.

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
