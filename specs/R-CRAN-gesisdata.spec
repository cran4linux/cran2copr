%global packname  gesisdata
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Reproducible Data Retrieval from the GESIS Data Archive

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RSelenium >= 1.7.1
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-RSelenium >= 1.7.1
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-tools 
Requires:         R-utils 

%description
Reproducible, programmatic retrieval of datasets from the GESIS Data
Archive.  The GESIS Data Archive <https://search.gesis.org> makes
available thousands of invaluable datasets, but researchers using these
datasets are caught in a bind.  The archive's terms and conditions bar
dissemination of downloaded datasets to third parties, but to ensure that
one's work can be reproduced, assessed, and built upon by others, one must
provide access to the raw data one has employed.  The 'gesisdata' package
cuts this knot by providing registered users with programmatic,
reproducible access to GESIS datasets from within 'R'.

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
