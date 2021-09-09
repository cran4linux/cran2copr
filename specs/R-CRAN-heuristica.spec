%global __brp_check_rpaths %{nil}
%global packname  heuristica
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Heuristics Including Take the Best and Unit-Weight Linear

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-Hmisc 

%description
Implements various heuristics like Take The Best and unit-weight linear,
which do two-alternative choice: which of two objects will have a higher
criterion?  Also offers functions to assess performance, e.g. percent
correct across all row pairs in a data set and finding row pairs where
models disagree. New models can be added by implementing a fit and predict
function-- see vignette.  Take The Best was first described in:
Gigerenzer, G. & Goldstein, D. G. (1996)
<doi:10.1037/0033-295X.103.4.650>.  All of these heuristics were run on
many data sets and analyzed in: Gigerenzer, G., Todd, P. M., & the ABC
Group (1999). <ISBN:978-0195143812>.

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
