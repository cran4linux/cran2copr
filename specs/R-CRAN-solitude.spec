%global __brp_check_rpaths %{nil}
%global packname  solitude
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          An Implementation of Isolation Forest

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-igraph >= 1.2.2
BuildRequires:    R-CRAN-data.table >= 1.11.4
BuildRequires:    R-CRAN-lgr >= 0.3.4
BuildRequires:    R-CRAN-future.apply >= 0.2.0
BuildRequires:    R-CRAN-ranger >= 0.11.0
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-igraph >= 1.2.2
Requires:         R-CRAN-data.table >= 1.11.4
Requires:         R-CRAN-lgr >= 0.3.4
Requires:         R-CRAN-future.apply >= 0.2.0
Requires:         R-CRAN-ranger >= 0.11.0

%description
Isolation forest is anomaly detection method introduced by the paper
Isolation based Anomaly Detection (Liu, Ting and Zhou
<doi:10.1145/2133360.2133363>).

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
