%global packname  gconsensus
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Consensus Value Constructor

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.0
BuildRequires:    R-utils >= 3.4.4
BuildRequires:    R-graphics >= 3.4.0
BuildRequires:    R-stats >= 3.4.0
Requires:         R-MASS >= 7.0
Requires:         R-utils >= 3.4.4
Requires:         R-graphics >= 3.4.0
Requires:         R-stats >= 3.4.0

%description
An implementation of the International Bureau of Weights and Measures
(BIPM) generalized consensus estimators used to assign the reference value
in a key comparison exercise. This can also be applied to any
interlaboratory study. Given a set of different sources, primary
laboratories or measurement methods this package provides an evaluation of
the variance components according to the selected statistical method for
consensus building. It also implements the comparison among different
consensus builders and evaluates the participating method or sources
against the consensus reference value. Based on a diverse set of
references, Graybill-Deal (1959) <doi:10.2307/2527652>, DerSimonian-Laird
(1986) <doi:10.1016/0197-2456(86)90046-2>, Vangel-Ruhkin (1999)
<doi:10.1111/j.0006-341X.1999.00129.x>, for a complete list of references
look at the reference section in the package documentation.

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
