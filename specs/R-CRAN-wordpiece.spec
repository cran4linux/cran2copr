%global __brp_check_rpaths %{nil}
%global packname  wordpiece
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          R Implementation of Wordpiece Tokenization

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringi >= 1.0
BuildRequires:    R-CRAN-digest >= 0.6.5
BuildRequires:    R-CRAN-rappdirs >= 0.3
BuildRequires:    R-CRAN-purrr >= 0.2.3
Requires:         R-CRAN-stringi >= 1.0
Requires:         R-CRAN-digest >= 0.6.5
Requires:         R-CRAN-rappdirs >= 0.3
Requires:         R-CRAN-purrr >= 0.2.3

%description
Apply 'Wordpiece' (<arXiv:1609.08144>) tokenization to input text, given
an appropriate vocabulary. The 'BERT' (<arXiv:1810.04805>) tokenization
conventions are used by default.

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
