%global __brp_check_rpaths %{nil}
%global packname  preregr
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Specify (Pre)Registrations and Export Them Human- And Machine-Readably

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0
BuildRequires:    R-CRAN-yaml >= 2.2
BuildRequires:    R-CRAN-jsonlite >= 1.7
BuildRequires:    R-CRAN-rmdpartials >= 0.5.8
Requires:         R-CRAN-cli >= 3.0
Requires:         R-CRAN-yaml >= 2.2
Requires:         R-CRAN-jsonlite >= 1.7
Requires:         R-CRAN-rmdpartials >= 0.5.8

%description
Preregistrations, or more generally, registrations, enable explicit
timestamped and (often but not necessarily publicly) frozen documentation
of plans and expectations as well as decisions and justifications. In
research, preregistrations are commonly used to clearly document plans and
facilitate justifications of deviations from those plans, as well as
decreasing the effects of publication bias by enabling identification of
research that was conducted but not published. Like reporting guidelines,
(pre)registration forms often have specific structures that facilitate
systematic reporting of important items. The 'preregr' package facilitates
specifying (pre)registrations in R and exporting them to a human-readable
format (using R Markdown partials or exporting to an 'HTML' file) as well
as human-readable embedded data (using 'JSON'), as well as importing such
exported (pre)registration specifications from such embedded 'JSON'.

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
