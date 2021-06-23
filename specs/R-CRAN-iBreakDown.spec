%global __brp_check_rpaths %{nil}
%global packname  iBreakDown
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Model Agnostic Instance Level Variable Attributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
Model agnostic tool for decomposition of predictions from black boxes.
Supports additive attributions and attributions with interactions. The
Break Down Table shows contributions of every variable to a final
prediction. The Break Down Plot presents variable contributions in a
concise graphical way. This package works for classification and
regression models. It is an extension of the 'breakDown' package (Staniak
and Biecek 2018) <doi:10.32614/RJ-2018-072>, with new and faster
strategies for orderings. It supports interactions in explanations and has
interactive visuals (implemented with 'D3.js' library). The methodology
behind is described in the 'iBreakDown' article (Gosiewska and Biecek
2019) <arXiv:1903.11420> This package is a part of the 'DrWhy.AI' universe
(Biecek 2018) <arXiv:1806.08915>.

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
