%global __brp_check_rpaths %{nil}
%global packname  downloadthis
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Implement Download Buttons in 'rmarkdown'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-bsplus 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-bsplus 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-ggplot2 

%description
Implement download buttons in HTML output from 'rmarkdown' without the
need for 'runtime:shiny'.

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
