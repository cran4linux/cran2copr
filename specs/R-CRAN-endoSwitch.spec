%global __brp_check_rpaths %{nil}
%global packname  endoSwitch
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Endogenous Switching Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.6.1
BuildRequires:    R-CRAN-msm >= 1.6.7
BuildRequires:    R-CRAN-maxLik >= 1.3.6
BuildRequires:    R-CRAN-data.table >= 1.12.2
Requires:         R-stats >= 3.6.1
Requires:         R-CRAN-msm >= 1.6.7
Requires:         R-CRAN-maxLik >= 1.3.6
Requires:         R-CRAN-data.table >= 1.12.2

%description
Maximum likelihood estimation of endogenous switching regression models
from Heckman (1979) <doi:10.2307/1912352> and estimation of treatment
effects.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
