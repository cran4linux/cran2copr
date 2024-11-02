%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcollectadhd
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Data Sets Containing ADHD Related Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch

%description
A collection of data sets relating to ADHD (Attention Deficit
Hyperactivity Disorder) which have been sourced from other packages on
CRAN or from publications on other websites such as Kaggle
<http://www.kaggle.com/>.The package also includes some simple functions
for analysing data sets. The data sets and descriptions of the data sets
may differ from what is on CRAN or other source websites. The aim of this
package is to bring together data sets from a variety of ADHD research
publications. This package would be useful for those interested in finding
out what research has been done on the topic of ADHD, or those interested
in comparing the results from different existing works. I started this
project because I wanted to put together a collection of the data sets
relevant to ADHD research, which I have a personal interest in. This work
was conducted with the support of my mentor within the Global Talent
Mentoring platform. <https://globaltalentmentoring.org/>.

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
