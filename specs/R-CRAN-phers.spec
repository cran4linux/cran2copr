%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phers
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Phenotype Risk Scores

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 3.3.1
BuildRequires:    R-CRAN-BEDMatrix >= 2.0.3
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-data.table >= 1.5.0
BuildRequires:    R-CRAN-iterators >= 1.0.14
Requires:         R-CRAN-survival >= 3.3.1
Requires:         R-CRAN-BEDMatrix >= 2.0.3
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-data.table >= 1.5.0
Requires:         R-CRAN-iterators >= 1.0.14

%description
Use phenotype risk scores based on linked clinical and genetic data to
study Mendelian disease and rare genetic variants. See Bastarache et al.
2018 <doi:10.1126/science.aal4043>.

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
