%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bain
%global packver   0.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Bayes Factors for Informative Hypotheses

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lavaan 
Requires:         R-stats 
Requires:         R-CRAN-lavaan 

%description
Computes approximated adjusted fractional Bayes factors for equality,
inequality, and about equality constrained hypotheses. For a tutorial on
this method, see Hoijtink, Mulder, van Lissa, & Gu, (2019)
<doi:10.31234/osf.io/v3shc>. For applications in structural equation
modeling, see: Van Lissa, Gu, Mulder, Rosseel, Van Zundert, & Hoijtink,
(2021) <doi:10.1080/10705511.2020.1745644>. For the statistical
underpinnings, see Gu, Mulder, and Hoijtink (2018)
<doi:10.1111/bmsp.12110>; Hoijtink, Gu, & Mulder, J. (2019)
<doi:10.1111/bmsp.12145>; Hoijtink, Gu, Mulder, & Rosseel, (2019)
<doi:10.31234/osf.io/q6h5w>.

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
