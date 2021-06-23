%global __brp_check_rpaths %{nil}
%global packname  elisr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Likert Scaling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.0
Requires:         R-stats >= 4.0.0

%description
An alternative to Exploratory Factor Analysis (EFA) for metrical data in
R. Drawing on characteristics of classical test theory, Exploratory Likert
Scaling (ELiS) supports the user exploring multiple one-dimensional data
structures. In common research practice, however, EFA remains the go-to
method to uncover the (underlying) structure of a data set. Orthogonal
dimensions and the potential of overextraction are often accepted as side
effects. As described in Müller-Schneider (2001)
<doi:10.1515/zfsoz-2001-0404>), ELiS confronts these problems. As a
result, 'elisr' provides the platform to fully exploit the exploratory
potential of the multiple scaling approach itself.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
