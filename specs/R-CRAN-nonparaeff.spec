%global __brp_check_rpaths %{nil}
%global packname  nonparaeff
%global packver   0.5-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.8
Release:          2%{?dist}%{?buildtag}
Summary:          Nonparametric Methods for Measuring Efficiency and Productivity

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-pwt 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-pwt 

%description
This package contains functions for measuring efficiency and productivity
of decision making units (DMUs) under the framework of Data Envelopment
Analysis (DEA) and its variations.

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

%files
%{rlibdir}/%{packname}
