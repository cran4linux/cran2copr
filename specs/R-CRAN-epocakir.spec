%global __brp_check_rpaths %{nil}
%global packname  epocakir
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          1%{?dist}%{?buildtag}
Summary:          Clinical Coding of Patients with Kidney Disease

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-tidyr >= 1.1.1
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.1
BuildRequires:    R-CRAN-units >= 0.7
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-tidyr >= 1.1.1
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.1
Requires:         R-CRAN-units >= 0.7
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 

%description
Clinical coding and diagnosis of patients with kidney using clinical
practice guidelines. The guidelines used are the evidence-based KDIGO
guidelines, see <https://kdigo.org/guidelines/> for more information. This
package covers acute kidney injury (AKI), anemia, and chronic liver
disease (CKD).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
