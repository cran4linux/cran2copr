%global packname  LSX
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Model for Semisupervised Text Analysis Based on Word Embeddings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quanteda >= 2.0
BuildRequires:    R-CRAN-quanteda.textmodels 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-rsvd 
BuildRequires:    R-CRAN-rsparse 
BuildRequires:    R-CRAN-proxyC 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-quanteda >= 2.0
Requires:         R-CRAN-quanteda.textmodels 
Requires:         R-methods 
Requires:         R-CRAN-digest 
Requires:         R-Matrix 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-rsvd 
Requires:         R-CRAN-rsparse 
Requires:         R-CRAN-proxyC 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-e1071 

%description
A word embeddings-based semisupervised models for document scaling
Watanabe (2017) <doi:10.1177/0267323117695735>. LSS allows users to
analyze large and complex corpora on arbitrary dimensions with seed words
exploiting efficiency of word embeddings (SVD, Glove).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
