%global __brp_check_rpaths %{nil}
%global packname  gluedown
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Wrap Vectors in Markdown Formatting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-glue >= 1.3.1
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-glue >= 1.3.1

%description
Ease the transition between R vectors and markdown text. With 'gluedown'
and 'rmarkdown', users can create traditional vectors in R, glue those
strings together with the markdown syntax, and print those formatted
vectors directly to the document. This package primarily uses GitHub
Flavored Markdown (GFM), an offshoot of the unambiguous CommonMark
specification by John MacFarlane (2019) <https://spec.commonmark.org/>.

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
