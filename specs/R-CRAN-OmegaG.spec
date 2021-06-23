%global __brp_check_rpaths %{nil}
%global packname  OmegaG
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Omega-Generic: Composite Reliability of Multidimensional Measures

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.50
Requires:         R-core >= 2.50
BuildArch:        noarch

%description
It is a computer tool to estimate the item-sum score's reliability
(composite reliability, CR) in multidimensional scales with overlapping
items. An item that measures more than one domain construct is called an
overlapping item. The estimation is based on factor models allowing
unlimited cross-factor loadings such as exploratory structural equation
modeling (ESEM) and Bayesian structural equation modeling (BSEM). The
factor models include correlated-factor models and bi-factor models.
Specifically for bi-factor models, a type of hierarchical factor model,
the package estimates the CR hierarchical subscale/hierarchy and CR
subscale/scale total. The CR estimator 'Omega-generic' was proposed by
Mai, Srivastava, and Krull (2021)
<https://whova.com/embedded/subsession/enars_202103/1450751/1452993/>. The
current version can only handle continuous data. Yujiao Mai contributes to
the algorithms, R programming, and application example. Deo Kumar
Srivastava contributes to the algorithms and the application example.
Kevin R. Krull contributes to the application example. The package
'OmegaG' was sponsored by American Lebanese Syrian Associated Charities
(ALSAC). However, the contents of 'OmegaG' do not necessarily represent
the policy of the ALSAC.

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
