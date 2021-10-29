%global __brp_check_rpaths %{nil}
%global packname  tosca
%global packver   0.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Statistical Content Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.7.3
BuildRequires:    R-CRAN-WikipediR >= 1.5.0
BuildRequires:    R-CRAN-lda >= 1.4.2
BuildRequires:    R-CRAN-quanteda >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-data.table >= 1.11.4
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-tm >= 0.7.5
BuildRequires:    R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-lubridate >= 1.7.3
Requires:         R-CRAN-WikipediR >= 1.5.0
Requires:         R-CRAN-lda >= 1.4.2
Requires:         R-CRAN-quanteda >= 1.4.0
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-data.table >= 1.11.4
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-tm >= 0.7.5
Requires:         R-CRAN-htmltools >= 0.3.6

%description
A framework for statistical analysis in content analysis. In addition to a
pipeline for preprocessing text corpora and linking to the latent
Dirichlet allocation from the 'lda' package, plots are offered for the
descriptive analysis of text corpora and topic models. In addition, an
implementation of Chang's intruder words and intruder topics is provided.
Sample data for the vignette is included in the toscaData package, which
is available on gitHub: <https://github.com/Docma-TU/toscaData>.

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
