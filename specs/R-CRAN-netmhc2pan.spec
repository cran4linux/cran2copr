%global packname  netmhc2pan
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'NetMHCIIpan'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-assertive 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-testit 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-assertive 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-testit 
Requires:         R-CRAN-tibble 

%description
The field of immunology benefits from software that can predict which
peptide sequences trigger an immune response. 'NetMHCIIpan' is a such a
tool: it predicts the binding strength of a short peptide to a Major
Histocompatibility Complex class II (MHC-II) molecule. 'NetMHCIIpan' can
be used from a web server at
<https://services.healthtech.dtu.dk/service.php?NetMHCIIpan-3.2/> or from
the command-line, using a local installation. This package allows to call
'NetMHCIIpan' from R.

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
