%global __brp_check_rpaths %{nil}
%global packname  ioanalysis
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Input Output Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-lpSolve 
Requires:         R-utils 

%description
Calculates fundamental IO matrices (Leontief, Wassily W. (1951)
<doi:10.1038/scientificamerican1051-15>); within period analysis via
various rankings and coefficients (Sonis and Hewings (2006)
<doi:10.1080/09535319200000013>, Blair and Miller (2009)
<ISBN:978-0-521-73902-3>, Antras et al (2012) <doi:10.3386/w17819>,
Hummels, Ishii, and Yi (2001) <doi:10.1016/S0022-1996(00)00093-3>); across
period analysis with impact analysis (Dietzenbacher, van der Linden, and
Steenge (2006) <doi:10.1080/09535319300000017>, Sonis, Hewings, and Guo
(2006) <doi:10.1080/09535319600000002>); and a variety of table operators.

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
