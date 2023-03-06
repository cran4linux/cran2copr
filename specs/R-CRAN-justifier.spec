%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  justifier
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Human and Machine-Readable Justifications and Justified Decisions Based on 'YAML'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.2.0
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.0
BuildRequires:    R-CRAN-data.tree >= 0.7.8
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-DiagrammeRsvg >= 0.1
BuildRequires:    R-CRAN-yum >= 0.0.1
Requires:         R-CRAN-yaml >= 2.2.0
Requires:         R-CRAN-DiagrammeR >= 1.0.0
Requires:         R-CRAN-data.tree >= 0.7.8
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-DiagrammeRsvg >= 0.1
Requires:         R-CRAN-yum >= 0.0.1

%description
Leverages the 'yum' package to implement a 'YAML' ('YAML Ain't Markup
Language', a human friendly standard for data serialization; see
<https:yaml.org>) standard for documenting justifications, such as for
decisions taken during the planning, execution and analysis of a study or
during the development of a behavior change intervention as illustrated by
Marques & Peters (2019) <doi:10.17605/osf.io/ndxha>. These justifications
are both human- and machine-readable, facilitating efficient extraction
and organisation.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
