%global packname  tinytex
%global packver   0.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16
Release:          1%{?dist}
Summary:          Helper Functions to Install and Maintain 'TeX Live', and Compile'LaTeX' Documents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xfun >= 0.5
Requires:         R-CRAN-xfun >= 0.5

%description
Helper functions to install and maintain the 'LaTeX' distribution named
'TinyTeX' (<https://yihui.name/tinytex/>), a lightweight, cross-platform,
portable, and easy-to-maintain version of 'TeX Live'. This package also
contains helper functions to compile 'LaTeX' documents, and install
missing 'LaTeX' packages automatically.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
