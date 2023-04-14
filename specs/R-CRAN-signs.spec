%global __brp_check_rpaths %{nil}
%global packname  signs
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Insert Proper Minus Signs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-scales 

%description
Provides convenience functions to replace hyphen-minuses (ASCII 45) with
proper minus signs (Unicode character 2212). The true minus matches the
plus symbol in width, line thickness, and height above the baseline. It
was designed for mathematics, looks better in presentation, and is
understood properly by screen readers.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
