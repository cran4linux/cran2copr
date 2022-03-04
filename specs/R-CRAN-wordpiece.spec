%global __brp_check_rpaths %{nil}
%global packname  wordpiece
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          R Implementation of Wordpiece Tokenization

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-memoise >= 2.0.0
BuildRequires:    R-CRAN-fastmatch >= 1.1
BuildRequires:    R-CRAN-wordpiece.data >= 1.0.2
BuildRequires:    R-CRAN-dlr >= 1.0.0
BuildRequires:    R-CRAN-piecemaker >= 1.0.0
BuildRequires:    R-CRAN-stringi >= 1.0
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-memoise >= 2.0.0
Requires:         R-CRAN-fastmatch >= 1.1
Requires:         R-CRAN-wordpiece.data >= 1.0.2
Requires:         R-CRAN-dlr >= 1.0.0
Requires:         R-CRAN-piecemaker >= 1.0.0
Requires:         R-CRAN-stringi >= 1.0
Requires:         R-CRAN-rlang 

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
