%global __brp_check_rpaths %{nil}
%global packname  InformativeCensoring
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Imputation for Informative Censoring

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-survival >= 2.36.1
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-boot 
BuildRequires:    R-parallel 
Requires:         R-survival >= 2.36.1
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-boot 
Requires:         R-parallel 

%description
Multiple Imputation for Informative Censoring. This package implements two
methods. Gamma Imputation described in <DOI:10.1002/sim.6274> and Risk
Score Imputation described in <DOI:10.1002/sim.3480>.

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
