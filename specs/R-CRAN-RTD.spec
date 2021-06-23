%global __brp_check_rpaths %{nil}
%global packname  RTD
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simple TD API Client

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.2.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppMsgPack 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-readr >= 1.2.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-RcppMsgPack 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-purrr 

%description
Upload R data.frame to Arm Treasure Data, see
<https://www.treasuredata.com/>. You can execute database or table
handling for resources on Arm Treasure Data.

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
