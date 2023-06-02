%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autoScorecard
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fully Automatic Generation of Scorecards

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-discretization 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-corrplot 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-discretization 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-corrplot 

%description
Provides an efficient suite of R tools for scorecard modeling, analysis,
and visualization. Including equal frequency binning, equidistant binning,
K-means binning, chi-square binning, decision tree binning, data
screening, manual parameter modeling, fully automatic generation of
scorecards, etc. This package is designed to make scorecard development
easier and faster. References include: 1. <http://shichen.name/posts/>. 2.
Dong-feng Li(Peking University),Class PPT. 3.
<https://zhuanlan.zhihu.com/p/389710022>. 4.
<https://www.zhangshengrong.com/p/281oqR9JNw/>.

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
