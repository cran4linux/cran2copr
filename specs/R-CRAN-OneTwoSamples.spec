%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OneTwoSamples
%global packver   1.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Deal with One and Two (Normal) Samples

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
We introduce an R function one_two_sample() which can deal with one and
two (normal) samples, Ying-Ying Zhang, Yi Wei (2012)
<doi:10.2991/asshm-13.2013.29>. For one normal sample x, the function
reports descriptive statistics, plot, interval estimation and test of
hypothesis of x. For two normal samples x and y, the function reports
descriptive statistics, plot, interval estimation and test of hypothesis
of x and y, respectively. It also reports interval estimation and test of
hypothesis of mu1-mu2 (the difference of the means of x and y) and
sigma1^2 / sigma2^2 (the ratio of the variances of x and y), tests whether
x and y are from the same population, finds the correlation coefficient of
x and y if x and y have the same length.

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
