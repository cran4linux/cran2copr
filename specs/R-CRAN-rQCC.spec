%global __brp_check_rpaths %{nil}
%global packname  rQCC
%global packver   1.20.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.20.7
Release:          2%{?dist}%{?buildtag}
Summary:          Robust Quality Control Chart

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch

%description
Constructs robust quality control chart based on the median or
Hodges-Lehmann estimator (location) and the median absolute deviation
(MAD) or Shamos estimator (scale). These estimators are all unbiased with
a sample of finite size. For more details, see Park, Kim and Wang (2020)
<doi:10.1080/03610918.2019.1699114>. In addition, using this package, the
conventional quality control charts such as X-bar, S and R charts are also
easily constructed. This work was partially supported by the National
Research Foundation of Korea (NRF) grant funded by the Korea government
(NRF-2017R1A2B4004169).

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
