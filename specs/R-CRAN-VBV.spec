%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VBV
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          The Generalized Berlin Method for Time Series Decomposition

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Time series decomposition for univariate time series using the
"Verallgemeinerte Berliner Verfahren" (Generalized Berlin Method) as
described in 'Kontinuierliche Messgrößen und Stichprobenstrategien in Raum
und Zeit mit Anwendungen in den Natur-, Umwelt-, Wirtschafts- und
Finanzwissenschaften', by Hebbel and Steuer, Springer Berlin Heidelberg,
2022 <doi:10.1007/978-3-662-65638-9>, or 'Decomposition of Time Series
using the Generalised Berlin Method (VBV)' by Hebbel and Steuer, in Jan
Beran, Yuanhua Feng, Hartmut Hebbel (Eds.): Empirical Economic and
Financial Research - Theory, Methods and Practice, Festschrift in Honour
of Prof. Siegfried Heiler. Series: Advanced Studies in Theoretical and
Applied Econometrics. Springer 2014, p. 9-40.

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
