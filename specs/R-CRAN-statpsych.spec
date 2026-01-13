%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statpsych
%global packver   1.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Psychologists

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mnonr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-mathjaxr 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-mnonr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-mathjaxr 

%description
Implements confidence interval and sample size methods that are especially
useful in psychological research. The methods can be applied in 1-group,
2-group, paired-samples, and multiple-group designs and to a variety of
parameters including means, medians, proportions, slopes, standardized
mean differences, standardized linear contrasts of means, plus several
measures of correlation and association. Confidence interval and sample
size functions are given for single parameters as well as differences,
ratios, and linear contrasts of parameters. The sample size functions can
be used to approximate the sample size needed to estimate a parameter or
function of parameters with desired confidence interval precision or to
perform a variety of hypothesis tests (directional two-sided, equivalence,
superiority, noninferiority) with desired power. For details see:
Statistical Methods for Psychologists, Volumes 1 – 4,
<https://dgbonett.sites.ucsc.edu/>.

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
