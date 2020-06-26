%global packname  r2shortcode
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Shorten Package Function Names

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 

%description
When creating a package, authors may sometimes struggle with coming up
with easy and straightforward function names, and at the same time hoping
that other packages do not already have the same function names. In trying
to meet this goal, sometimes, function names are not descriptive enough
and may confuse the potential users. The purpose of this package is to
serve as a package function short form generator and also provide
shorthand names for other functions. Having this package will entice
authors to create long function names without the fear of users not
wanting to use their packages because of the long names. In a way,
everyone wins - the authors can use long descriptive function names, and
the users can use this package to make short functions names while still
using the package in question.

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
