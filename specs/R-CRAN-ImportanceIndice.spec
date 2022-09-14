%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ImportanceIndice
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Data Through of Percentage of Importance Indice and Its Derivations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-crayon 

%description
The Percentage of Importance Indice (Percentage_I.I.) bases in magnitudes,
frequencies, and distributions of occurrence of an event (DEMOLIN-LEITE,
2021) <http://cjascience.com/index.php/CJAS/article/view/1009/1350>. This
index can detect the key loss sources (L.S) and solution sources (S.S.),
classifying them according to their importance in terms of loss or income
gain, on the productive system. The Percentage_I.I. = [(ks1 x c1 x
ds1)/SUM (ks1 x c1 x ds1) + (ks2 x c2 x ds2) + (ksn x cn x dsn)] x 100.
key source (ks) is obtained using simple regression analysis and magnitude
(abundance). Constancy (c) is SUM of occurrence of L.S. or S.S. on the
samples (absence = 0 or presence = 1), and distribution source (ds) is
obtained using chi-square test. This index has derivations: i.e., i) Loss
estimates and solutions effectiveness and ii) Attention and non-attention
levels (DEMOLIN-LEITE,2024) <DOI: 10.1590/1519-6984.253215>.

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
