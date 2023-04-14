%global __brp_check_rpaths %{nil}
%global packname  Dowd
%global packver   0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12
Release:          3%{?dist}%{?buildtag}
Summary:          Functions Ported from 'MMR2' Toolbox Offered in Kevin Dowd'sBook Measuring Market Risk

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bootstrap 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-forecast 
Requires:         R-CRAN-bootstrap 
Requires:         R-MASS 
Requires:         R-CRAN-forecast 

%description
'Kevin Dowd's' book Measuring Market Risk is a widely read book in the
area of risk measurement by students and practitioners alike. As he
claims, 'MATLAB' indeed might have been the most suitable language when he
originally wrote the functions, but, with growing popularity of R it is
not entirely valid. As 'Dowd's' code was not intended to be error free and
were mainly for reference, some functions in this package have inherited
those errors. An attempt will be made in future releases to identify and
correct them. 'Dowd's' original code can be downloaded from
www.kevindowd.org/measuring-market-risk/. It should be noted that 'Dowd'
offers both 'MMR2' and 'MMR1' toolboxes. Only 'MMR2' was ported to R.
'MMR2' is more recent version of 'MMR1' toolbox and they both have mostly
similar function. The toolbox mainly contains different parametric and non
parametric methods for measurement of market risk as well as backtesting
risk measurement methods.

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
