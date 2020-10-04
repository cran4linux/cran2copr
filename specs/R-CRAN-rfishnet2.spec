%global packname  rfishnet2
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Data Analysis for FishNet2 Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-pracma >= 2.2.5
BuildRequires:    R-CRAN-rworldmap >= 1.3.6
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-sf >= 0.8.0
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-pracma >= 2.2.5
Requires:         R-CRAN-rworldmap >= 1.3.6
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-sf >= 0.8.0

%description
Provides data processing and summarization of data from FishNet2.net in
text and graphical outputs. Allows efficient filtering of information and
data cleaning.

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
