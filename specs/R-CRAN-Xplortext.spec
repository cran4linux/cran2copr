%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Xplortext
%global packver   1.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Analysis of Textual Data

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-FactoMineR >= 2.11
BuildRequires:    R-CRAN-tm >= 0.7.14
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-flashClust 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-FactoMineR >= 2.11
Requires:         R-CRAN-tm >= 0.7.14
Requires:         R-CRAN-ape 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-flashClust 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggrepel 
Requires:         R-graphics 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-slam 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-vegan 

%description
Provides a set of functions devoted to multivariate exploratory statistics
on textual data. Classical methods such as correspondence analysis and
agglomerative hierarchical clustering are available. Chronologically
constrained agglomerative hierarchical clustering enriched with
labelled-by-words trees is offered. Given a division of the corpus into
parts, their characteristic words and documents are identified. Further,
accessing to 'FactoMineR' functions is very easy. Two of them are relevant
in textual domain. MFA() addresses multiple lexical table allowing
applications such as dealing with multilingual corpora as well as
simultaneously analyzing both open-ended and closed questions in surveys.
See <http://xplortext.unileon.es> for examples.

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
