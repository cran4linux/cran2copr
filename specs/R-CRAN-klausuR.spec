%global __brp_check_rpaths %{nil}
%global packname  klausuR
%global packver   0.12-14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.14
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Choice Test Evaluation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-xtable 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-psych 

%description
A set of functions designed to quickly generate results of a multiple
choice test. Generates detailed global results, lists for anonymous
feedback and personalised result feedback (in LaTeX and/or PDF format), as
well as item statistics like Cronbach's alpha or disciminatory power.
'klausuR' also includes a plugin for the R GUI and IDE RKWard, providing
graphical dialogs for its basic features. The respective R package
'rkward' cannot be installed directly from a repository, as it is a part
of RKWard. To make full use of this feature, please install RKWard from
<https://rkward.kde.org> (plugins are detected automatically). Due to some
restrictions on CRAN, the full package sources are only available from the
project homepage.

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
