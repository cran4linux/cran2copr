%global __brp_check_rpaths %{nil}
%global packname  powerplus
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Exponentiation Operations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.45
BuildRequires:    R-CRAN-complexplus >= 2.0
BuildRequires:    R-Matrix >= 1.2.6
BuildRequires:    R-CRAN-expm >= 0.999.2
BuildRequires:    R-CRAN-phonTools >= 0.2.2.1
Requires:         R-MASS >= 7.3.45
Requires:         R-CRAN-complexplus >= 2.0
Requires:         R-Matrix >= 1.2.6
Requires:         R-CRAN-expm >= 0.999.2
Requires:         R-CRAN-phonTools >= 0.2.2.1

%description
Computation of matrix and scalar exponentiation.

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
