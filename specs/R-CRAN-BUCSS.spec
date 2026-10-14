%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BUCSS
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bias and Uncertainty Corrected Sample Size

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 3.0.3
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-withr >= 3.0.3
Requires:         R-CRAN-generics 
Requires:         R-graphics 
Requires:         R-stats 

%description
Implements sample size planning for a future study from the summary
statistics of a prior study, correcting the prior effect for publication
bias and uncertainty so the planned study attains its target statistical
power more reliably than methods that take a sample effect size at face
value. Planners cover the one-sample, paired, independent, and Welch t
tests; between-subjects analysis of variance and covariance;
within-subjects and split-plot analysis of variance; a regression
coefficient, the squared multiple correlation, and a subset of predictors;
the Pearson correlation; a two-group multivariate comparison; and the chi
square difference between nested models. The regression planners can treat
the predictors as fixed or as sampled, the within-subjects and split-plot
planners accept a sphericity correction, and each plan reports the effect
size it is built on. A simulation function audits how often a plan attains
its target power. The method is described in Anderson, Kelley, and Maxwell
(2017) <doi:10.1177/0956797617723724> and extended to replication studies
in Anderson and Kelley (2024) <doi:10.1037/met0000520>.

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
