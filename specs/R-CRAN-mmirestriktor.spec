%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mmirestriktor
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Informative Hypothesis Testing Web Applications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mmcards 
BuildRequires:    R-CRAN-restriktor 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mmcards 
Requires:         R-CRAN-restriktor 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 

%description
Offering enhanced statistical power compared to traditional hypothesis
testing methods, informative hypothesis testing allows researchers to
explicitly model their expectations regarding the relationships among
parameters. An important software tool for this framework is 'restriktor'.
The 'mmirestriktor' package provides 'shiny' web applications to implement
some of the basic functionality of 'restriktor'. The mmirestriktor()
function launches a 'shiny' application for fitting and analyzing models
with constraints. The FbarCards() function launches a card game
application which can help build intuition about informative hypothesis
testing. The iht_interpreter() helps interpret informative hypothesis
testing results based on guidelines in Vanbrabant and Rosseel (2020)
<doi:10.4324/9780429273872-14>.

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
