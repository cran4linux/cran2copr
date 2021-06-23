%global __brp_check_rpaths %{nil}
%global packname  clinspacy
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Clinical Natural Language Processing using 'spaCy', 'scispaCy', and 'medspaCy'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.16
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-reticulate >= 1.16
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-rappdirs 
Requires:         R-utils 
Requires:         R-CRAN-magrittr 

%description
Performs biomedical named entity recognition, Unified Medical Language
System (UMLS) concept mapping, and negation detection using the Python
'spaCy', 'scispaCy', and 'medspaCy' packages, and transforms extracted
data into a wide format for inclusion in machine learning models. The
development of the 'scispaCy' package is described by Neumann (2019)
<doi:10.18653/v1/W19-5034>. The 'medspacy' package uses 'ConText', an
algorithm for determining the context of clinical statements described by
Harkema (2009) <doi:10.1016/j.jbi.2009.05.002>. Clinspacy also supports
entity embeddings from 'scispaCy' and UMLS 'cui2vec' concept embeddings
developed by Beam (2018) <arXiv:1804.01486>.

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
