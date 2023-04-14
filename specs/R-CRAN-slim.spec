%global __brp_check_rpaths %{nil}
%global packname  slim
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Singular Linear Models for Longitudinal Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-stats 
Requires:         R-MASS >= 7.3
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-stats 

%description
Fits singular linear models to longitudinal data. Singular linear models
are useful when the number, or timing, of longitudinal observations may be
informative about the observations themselves. They are described in
Farewell (2010) <doi:10.1093/biomet/asp068>, and are extensions of the
linear increments model <doi:10.1111/j.1467-9876.2007.00590.x> to general
longitudinal data.

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
