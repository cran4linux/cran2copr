%global packname  DFA.CANCOR
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          2%{?dist}%{?buildtag}
Summary:          Linear Discriminant Function and Canonical Correlation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MVN 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-MVN 
Requires:         R-graphics 
Requires:         R-stats 

%description
Produces SPSS- and SAS-like output for linear discriminant function
analysis and canonical correlation analysis. The methods are described in
Manly & Alberto (2017, ISBN:9781498728966), Tabachnik & Fidell (2013,
ISBN-10:0-205-89081-4), and Venables & Ripley (2002, ISBN:0-387-95457-0).

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
