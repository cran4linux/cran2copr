%global __brp_check_rpaths %{nil}
%global packname  SegEnvIneq
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Environmental Inequality Indices Based on Segregation Measures

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-OasisR >= 3.0.2
BuildRequires:    R-CRAN-rgdal >= 1.4.8
BuildRequires:    R-CRAN-spdep >= 1.1.3
BuildRequires:    R-CRAN-rgeos >= 0.5.3
BuildRequires:    R-CRAN-outliers >= 0.14
Requires:         R-CRAN-OasisR >= 3.0.2
Requires:         R-CRAN-rgdal >= 1.4.8
Requires:         R-CRAN-spdep >= 1.1.3
Requires:         R-CRAN-rgeos >= 0.5.3
Requires:         R-CRAN-outliers >= 0.14

%description
A set of segregation-based indices and randomization methods to make
robust environmental inequality assessments, as described in Schaeffer and
Tivadar (2019) "Measuring Environmental Inequalities: Insights from the
Residential Segregation Literature" <doi:10.1016/j.ecolecon.2019.05.009>.

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
