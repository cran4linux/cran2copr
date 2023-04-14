%global __brp_check_rpaths %{nil}
%global packname  MEMSS
%global packver   0.9-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          3%{?dist}%{?buildtag}
Summary:          Data Sets from Mixed-Effects Models in S

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 0.999375.36
Requires:         R-CRAN-lme4 >= 0.999375.36

%description
Data sets and sample analyses from Pinheiro and Bates, "Mixed-effects
Models in S and S-PLUS" (Springer, 2000).

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
