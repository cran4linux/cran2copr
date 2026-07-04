%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  semanticfa
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Semantic Factor Analysis of Language Model Embeddings

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.41.0
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-reticulate >= 1.41.0
Requires:         R-CRAN-digest 
Requires:         R-CRAN-GPArotation 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-Rtsne 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-withr 

%description
Performs exploratory factor analysis on language model embeddings of
psychological scale items. Embeds item text with sentence transformers or
other language models, transforms the embeddings into item-by-item
similarity matrices, and extracts latent factor structure via standard
exploratory factor analysis. Supports embedding-adapted parallel analysis,
several similarity transforms (atomic reversed, SQuID centering,
mean-centered Pearson), and fit diagnostics tailored to embedding matrices
(TEFI, RMSR, CAF, McDonald's omega). The underlying methods are documented
with full citations in the corresponding function help pages. Returns
objects compatible with 'psych' and 'EFAtools' workflows.

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
