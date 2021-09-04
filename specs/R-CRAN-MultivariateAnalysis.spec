%global __brp_check_rpaths %{nil}
%global packname  MultivariateAnalysis
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Pacote Para Analise Multivariada

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-PCAmixdata 
BuildRequires:    R-CRAN-candisc 
BuildRequires:    R-CRAN-biotools 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-PCAmixdata 
Requires:         R-CRAN-candisc 
Requires:         R-CRAN-biotools 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ape 

%description
Package with multivariate analysis methodologies for experiment
evaluation. The package estimates dissimilarity measures, builds
dendrograms, obtains MANOVA, principal components, canonical variables,
etc. (Pacote com metodologias de analise multivariada para avaliação de
experimentos. O pacote estima medidas de dissimilaridade, construi de
dendogramas, obtem a MANOVA, componentes principais, variáveis canônicas,
etc.)

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
