%global __brp_check_rpaths %{nil}
%global packname  rebus
%global packver   0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Build Regular Expressions in a Human Readable Way

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rebus.base >= 0.0.3
BuildRequires:    R-CRAN-rebus.unicode >= 0.0.2
BuildRequires:    R-CRAN-rebus.datetimes 
BuildRequires:    R-CRAN-rebus.numbers 
Requires:         R-CRAN-rebus.base >= 0.0.3
Requires:         R-CRAN-rebus.unicode >= 0.0.2
Requires:         R-CRAN-rebus.datetimes 
Requires:         R-CRAN-rebus.numbers 

%description
Build regular expressions piece by piece using human readable code. This
package is designed for interactive use.  For package development, use the
rebus.* dependencies.

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
