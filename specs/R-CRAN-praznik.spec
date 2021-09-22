%global __brp_check_rpaths %{nil}
%global packname  praznik
%global packver   9.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          9.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Information-Based Feature Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10

%description
A toolbox of fast, native and parallel implementations of various
information-based importance criteria estimators and feature selection
filters based on them, inspired by the overview by Brown, Pocock, Zhao and
Lujan (2012) <https://www.jmlr.org/papers/v13/brown12a.html>. Contains,
among other, minimum redundancy maximal relevancy ('mRMR') method by Peng,
Long and Ding (2005) <doi:10.1109/TPAMI.2005.159>; joint mutual
information ('JMI') method by Yang and Moody (1999)
<https://papers.nips.cc/paper/1779-data-visualization-and-feature-selection-new-algorithms-for-nongaussian-data>;
double input symmetrical relevance ('DISR') method by Meyer and Bontempi
(2006) <doi:10.1007/11732242_9> as well as joint mutual information
maximisation ('JMIM') method by Bennasar, Hicks and Setchi (2015)
<doi:10.1016/j.eswa.2015.07.007>.

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
