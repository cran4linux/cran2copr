%global __brp_check_rpaths %{nil}
%global packname  catchr
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Taking the Pain Out of Catching and Handling Conditions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-purrr >= 0.2.0
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-purrr >= 0.2.0

%description
R has a unique way of dealing with warnings, errors, messages, and other
conditions, but it can often be troublesome to users coming from different
programming backgrounds. The purpose of this package is to provide
flexible and useful tools for handling R conditions with less hassle. In
order to lower the barrier of entry, keep code clean and readable, and
reduce the amount of typing required, `catchr` uses a very simple
domain-specific language that simplifies things on the front-end. This
package aims to maintain a continuous learning curve that lets new users
jump straight in to condition-handling, while simultaneously offering
depth and complexity for more advanced users.

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
