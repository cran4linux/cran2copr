%global __brp_check_rpaths %{nil}
%global packname  imfr
%global packver   0.1.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Download Data from the International Monetary Fund's Data API

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.2.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httr >= 1.2.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 

%description
Explore and download data from the International Monetary Fund's data API
<http://data.imf.org/>.

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
