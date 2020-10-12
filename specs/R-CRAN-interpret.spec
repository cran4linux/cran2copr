%global packname  interpret
%global packver   0.1.25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.25
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Interpretable Machine Learning Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
Package for training interpretable machine learning models. Historically,
the most interpretable machine learning models were not very accurate, and
the most accurate models were not very interpretable. Microsoft Research
has developed an algorithm called the Explainable Boosting Machine (EBM)
which has both high accuracy and interpretable characteristics. EBM uses
machine learning techniques like bagging and boosting to breathe new life
into traditional GAMs (Generalized Additive Models). This makes them as
accurate as random forests and gradient boosted trees, and also enhances
their intelligibility and editability. Details on the EBM algorithm can be
found in the paper by Rich Caruana, Yin Lou, Johannes Gehrke, Paul Koch,
Marc Sturm, and Noemie Elhadad (2015, <doi:10.1145/2783258.2788613>).

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
