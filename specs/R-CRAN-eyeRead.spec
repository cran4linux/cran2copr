%global __brp_check_rpaths %{nil}
%global packname  eyeRead
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Prepare/Analyse Eye Tracking Data for Reading

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-tidyr >= 1.0.0

%description
Functions to prepare and analyse eye tracking data of reading exercises.
The functions allow some basic data preparations and code fixations as
first and second pass. First passes can be further devided into forward
and reading. The package further allows for aggregating fixation times per
AOI or per AOI and per type of pass (first forward, first rereading,
second). These methods are based on Hyönä, Lorch, and Rinck (2003)
<doi:10.1016/B978-044451020-4/50018-9> and Hyönä, and Lorch (2004)
<doi:10.1016/j.learninstruc.2004.01.001>. It is also possible to convert
between metric length and visual degrees.

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
