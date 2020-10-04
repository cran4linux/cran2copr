%global packname  slider
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Sliding Window Functions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-warp 
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-glue 
Requires:         R-CRAN-warp 

%description
Provides type-stable rolling window functions over any R data type.
Cumulative and expanding windows are also supported. For more advanced
usage, an index can be used as a secondary vector that defines how sliding
windows are to be created.

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
