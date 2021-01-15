%global packname  Xplortext
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Analysis of Textual Data

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.53
BuildRequires:    R-CRAN-FactoMineR >= 2.4
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-stringi >= 1.5.3
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-flexclust >= 1.4.0
BuildRequires:    R-CRAN-flashClust >= 1.01.2
BuildRequires:    R-CRAN-ggrepel >= 0.9.0
BuildRequires:    R-CRAN-tm >= 0.7.8
BuildRequires:    R-CRAN-ggforce >= 0.3.2
BuildRequires:    R-CRAN-slam >= 0.1.48
BuildRequires:    R-CRAN-ggdendro >= 0.1.22
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-MASS >= 7.3.53
Requires:         R-CRAN-FactoMineR >= 2.4
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-stringi >= 1.5.3
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-flexclust >= 1.4.0
Requires:         R-CRAN-flashClust >= 1.01.2
Requires:         R-CRAN-ggrepel >= 0.9.0
Requires:         R-CRAN-tm >= 0.7.8
Requires:         R-CRAN-ggforce >= 0.3.2
Requires:         R-CRAN-slam >= 0.1.48
Requires:         R-CRAN-ggdendro >= 0.1.22
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

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
